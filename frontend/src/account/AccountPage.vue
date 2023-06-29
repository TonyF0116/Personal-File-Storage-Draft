<template>
  <div class="t1">{{ msg }}</div>

  <button class="b1" @click="togglePopup_login">Login</button>
  <button class="b2" @click="togglePopup_signup">Sign up</button>

  <transition name="fade">
    <div v-if="isPopupVisible" class="popup" @click.self="closePopup">
      <div class="popup-content">
        <div class="form-group">
          <label for="username">Username </label>
          <input type="text" name="username" id="username" v-model="username" @keyup.enter="enter_handler" />
        </div>
        <div class="form-group">
          <label for="password">Password </label>
          <input type="password" name="password" id="password" v-model="password" @keyup.enter="enter_handler" />
        </div>
        <div class="warning-content">{{ warning }}</div>
        <div v-if="login_pressed"><button class="b3" @click="login">Login</button></div>
        <div v-else><button class="b3" @click="signup">Sign up</button></div>
      </div>
    </div>
  </transition>
</template>

<script>
import SHA256 from 'crypto-js/sha256';
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:5000';


export default {
  data() {
    return {
      msg: "Welcome!",
      isPopupVisible: false,
      login_pressed: true,
      username: "",
      password: "",
      warning: ""
    }
  },
  methods: {
    // Handle enter pressed when user is in input box
    enter_handler() {
      if (this.login_pressed) {
        this.login()
      } else {
        this.signup()
      }
    },
    // Show login window when login is clicked
    togglePopup_login() {
      this.isPopupVisible = !this.isPopupVisible;
      this.login_pressed = true
    },
    // Show signup window when signup is clicked
    togglePopup_signup() {
      this.isPopupVisible = !this.isPopupVisible;
      this.login_pressed = false
    },
    // Close the pop up window and clear the input
    closePopup() {
      this.isPopupVisible = false;
      this.username = "";
      this.password = "";
      this.warning = "";
    },

    // Check for empty username and password
    check_empty() {
      if (this.username == "") {
        this.warning = "Username can not be empty"
        return
      }
      if (this.password == "") {
        this.warning = "Password can not be empty"
        return
      }
      return ""
    },
    login() {
      // Check if input is empty
      if (this.check_empty() != "") {
        return this.check_empty()
      }
      // Send login request with the input username and password hash
      axios.post('/account/login', {
        username: this.username,
        password: SHA256(this.password).toString()
      })
        .then(response => {
          // If a redirect request is received, then follow the redirect to the new website
          // Otherwise, a warning is received, so show the warning
          if (response.data[0] != "<") {  // Redirect request will send back an Html, which starts with a '<'
            this.warning = response.data
          }
          else {
            // document.body.innerHTML = response.data; no need for this line. The line below contains the effect of this line
            window.location.href = response.request.responseURL
          }
        });
    },
    signup() {
      // Check if input is empty
      if (this.check_empty() != "") {
        return this.check_empty()
      }
      // Send signup request with the input username and password hash
      axios.post('/account/signup', {
        username: this.username,
        password: SHA256(this.password).toString()
      })
        .then(response => {
          // If a redirect request is received, then follow the redirect to the new website
          // Otherwise, a warning is received, so show the warning
          if (response.data[0] != "<") {
            this.warning = response.data
          }
          else {
            window.location.href = response.request.responseURL
          }
        });
    }
  }
}
</script>



<style>
.warning-content {
  font-size: medium;
  color: red;
}

.form-group {
  position: relative;
  margin-bottom: 20px;
}

label {
  position: absolute;
  top: -10px;
  /* left: 10px; */
  font-weight: bold;
}

input {
  padding: 8px;
  margin-top: 10px;
}

.t1 {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 160px;
  font-size: xxx-large;
}

.b1 {
  background-color: #5750bc;
  border: none;
  color: white;
  padding: 15px 42px;
  text-align: center;
  font-size: 40px;
  border-radius: 10px;
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}


.b1:hover {
  background-color: #433ac5;
}

.b2 {
  background-color: #5750bc;
  border: none;
  color: white;
  padding: 15px 24px;
  text-align: center;
  font-size: 40px;
  border-radius: 10px;
  position: absolute;
  top: 55%;
  left: 50%;
  transform: translate(-50%, -50%);
}


.b2:hover {
  background-color: #433ac5;
}

.b3 {
  background-color: #276bff;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  font-size: 16px;
  /* position: absolute;
  top: 61%;
  left: 50%;
  transform: translate(-50%, -50%); */
  position: relative;
  margin-top: 10px;
  margin-left: 25%;
  border-radius: 8px;
}

.b3:hover {
  background-color: #1c5be5;
}

.t2 {
  text-align: center;
  font-size: xx-large;
}

.popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  background-color: #fff;
  padding: 60px;
  border-radius: 10px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
