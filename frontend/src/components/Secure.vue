<template>
  <div>
    <nav-bar></nav-bar>
    <h1>HELLO</h1>
    <h1>LOGGED: {{loggedin}}</h1>
    <div v-if="loggedin != true">
      <log-in></log-in>
    </div>
    <div v-else>
      <h2>LOGGED IN</h2>
    </div>
  </div>
</template>

<script>
import Login from "./Login.vue";
import NavBar from "./NavBar.vue";
import store from "../store/index";
export default {
  data: function () {
    return {
      loaded: false,
      message: "hello",
    };
  },
  components: {
    "log-in": Login,
    NavBar,
  },
  created: function () {
    store.dispatch("update_loggedin_status");
    this.loaded = true;
  },
  computed: {
    loggedin() {
      return this.$store.getters.is_logged_in;
    },
    s_message() {
      return this.$store.state.state_m;
    },
  },
};
</script>

<style>
</style>