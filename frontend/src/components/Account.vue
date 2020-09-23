<template>
  <div>
    <nav-bar></nav-bar>
    <h1>PROFILE</h1>
    <button @click="logout">LOG OUT</button>
  </div>
</template>

<script>
import Router from "../router/index";
import axios from "axios";
import store from "../store/index";
import NavBar from "./NavBar";
export default {
  methods: {
    logout: function () {
      const post_path = "http://localhost:5000/logout";
      axios.post(post_path).then((response) => {
        store.dispatch("update_loggedin_status");
        this.$router.push({ path: "/login" });
      });
    },
  },
  components: {
    NavBar,
  },
};
</script>

<style>
</style>