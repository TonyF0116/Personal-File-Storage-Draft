<template>
  <div class="t1">{{ msg }}</div>
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://127.0.0.1:5000';


export default {
  data() {
    return {
      msg: "Edit page",
    }
  },
  methods: {

  }
}
</script>



<style>
.t1 {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 160px;
  font-size: xxx-large;
}
</style>