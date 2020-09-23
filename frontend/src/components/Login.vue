/* eslist-disable */
<template>
  <div>
    <nav-bar></nav-bar>
    <div v-if="show_create_account">
      <create-account v-on:maybe_created="created_handler"></create-account>
      <h4 @click="show_create_account = false">Already have an account? Login.</h4>
    </div>
    <div v-else>
      <div class="container justify-content-center">
        <h1>HELLO LOG IN HERE</h1>
        <div class="row">
          <div class="col">
            <label for="username">USERNAME</label>
            <input v-model="username" type="text" name="username" id="username" />
          </div>
        </div>
        <div class="row">
          <div class="col">
            <label for="password">PASSWORD</label>
            <input v-model="password" type="password" name="password" id="password" />
          </div>
        </div>
        <div class="row">
          <div class="col">
            <div class="btn-group">
              <button type="button" class="btn btn-primary" @click="login">LOG IN</button>
            </div>
            <h2>USERNAME: {{username}}</h2>
            <h2>PASSWORD: {{password}}</h2>
          </div>
        </div>
      </div>
      <h4 @click="show_create_account = true">Create account</h4>
    </div>
  </div>
</template>

<script>
import Router from "vue-router";
import axios from "axios";
import store from "../store/index";
import NavBar from "./NavBar.vue";
import CreateAccount from "./CreateAccount";
export default {
  data: function () {
    return {
      show_create_account: true,
      message: "TEST",
      loggedin: false,
      username: "",
      password: "",
    };
  },
  methods: {
    bool_switch_create_account: function () {
      this.show_create_account != this.show_create_account;
    },
    created_handler: function (response) {
      const response_data = response.data.response;
      console.log(response_data);
      if (response_data.type == "success") {
        this.show_create_account = false;
      } else {
        alert(response_data.message);
      }
    },
    login: function () {
      var post_username = this.username;
      var post_password = this.password;
      const post_path = "http://localhost:5000/api/loginValidator";
      const post_data = {
        username: post_username,
        password: post_password,
      };
      axios({
        method: "post",
        url: post_path,
        data: post_data,
      }).then((response) => {
        console.log(response.data);
        this.$store.dispatch("update_loggedin_status");
        //IF LOGIN BREAKS CHECK THIS. IDEALY I WOULD BE USING A GETTER HERE. BUT THE STORE ISNT UPDATED FAST ENOUGH.
        //IT MIGHT BE FINE, BUT WE WILL SEE
        if (response.data.loggedin) {
          this.$router.push({ path: "/account" });
        }
      });
    },
  },
  components: {
    NavBar,
    CreateAccount,
  },
  computed: {
    login_status: function () {
      return store.state.loggedin;
    },
  },
};
</script>

<style scoped>
</style>