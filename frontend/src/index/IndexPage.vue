<template>
  <div class="t1">{{ msg }}</div>
  <h3 style="text-align: center;">Welcome, {{ username }}</h3>


  <button class="upload_button" @click="togglePopup">Upload</button>
  <ol>
    <li v-for="file in files">{{ file.filename }}<span style="margin-left: 50px;"> {{ file.last_modified }}</span></li>
  </ol>

  <transition name="fade">
    <div v-if="is_pop_up_visible" class="popup" @click.self="closePopup">
      <div class="popup-content">
        <input type="file" id="fileInput" @change="choose_file_clicked" accept=".jpg, .jpeg, .png, .pdf, .xls .xlsx">
        <label for="fileInput" class="choose_file_button">Choose File</label>

        <p>{{ choose_file_message }}</p>
        <div v-if="choose_file_message != '' && choose_file_message != 'Unaccepted file format'">
          <button class="submit_button" @click="upload_file">Submit</button>
          <p>{{ upload_msg }}</p>
        </div>


      </div>
    </div>
  </transition>
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:5000';


export default {
  mounted() {
    this.get_data()
  },
  data() {
    return {
      msg: "Index page",
      username: "",
      files: null,

      is_pop_up_visible: false,

      choose_file_message: "",
      upload_msg: "",

      file_to_upload: null,
      file_type: "",
    }
  },
  methods: {
    // Called on Index page mounted, get necessary user data
    get_data() {
      axios.post('/index/get_data', {
      }).then(response => {
        this.username = response.data['username'];
        this.files = response.data['files'];
      });
    },


    // Choose file handler, displays file name
    choose_file_clicked(event) {
      if (event.target.files.length > 0) {
        this.file_to_upload = event.target.files[0]

        const allowed_extensions = ['jpg', 'jpeg', 'png', 'pdf', 'xls', 'xlsx'];
        // Get the extension of the file to upload
        const cur_file_extension = this.file_to_upload.name.substring(this.file_to_upload.name.lastIndexOf('.') + 1).toLowerCase();
        console.log(cur_file_extension)

        // If file type is accepted, change the choose_file_message to the filename, and file_to_upload to this file
        // Otherwise, display "Unaccepted file format"
        if (allowed_extensions.includes(cur_file_extension)) {
          this.choose_file_message = this.file_to_upload.name;
          this.file_to_upload = this.file_to_upload
          this.file_type = cur_file_extension
        } else {
          this.choose_file_message = "Unaccepted file format"
          this.file_to_upload = null
        }
      } else {
        this.choose_file_message = '';
      }
    },

    // Build a form with file and file type, and send it to the server
    upload_file() {
      form = new FormData();
      form.append('file', this.file_to_upload);
      form.append('file_type', this.file_type);

      axios.post('/index/file_upload', form)
        .then(response => {
          this.upload_msg = response.data
        });
    },

    // Show pop up when Upload button is clicked
    togglePopup() {
      this.is_pop_up_visible = !this.is_pop_up_visible;
    },
    // Close pop up and clear related information
    closePopup() {
      this.is_pop_up_visible = false;
      this.choose_file_message = "";
      this.file_to_upload = null;
      this.upload_msg = "";
    },
  }
}
</script>



<style>
.upload_button {
  background-color: #5750bc;
  border: none;
  color: white;
  padding: 15px 24px;
  text-align: center;
  font-size: 24px;
  border-radius: 10px;
  position: absolute;
  top: 20%;
  left: 90%;
  transform: translate(-50%, -50%);
}

.choose_file_button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.submit_button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #fa0000;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

#fileInput {
  display: none;
  /* Hide the original file input button */
}

.t1 {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 160px;
  font-size: xxx-large;
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
  padding: auto;
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
