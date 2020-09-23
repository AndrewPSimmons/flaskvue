<template>
  <div>
    <div class="container">
      <h1>CREATE ACCOUNT</h1>
      <h3>HERE IS THE DATA {{create_acc_data}}</h3>
      <div class="row">
        <div class="col">
          <label for="first_name">First Name</label>
          <input v-model="create_acc_data.first_name" type="text" name="first_name" id="first_name" />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="last_name">Last Name</label>
          <input v-model="create_acc_data.last_name" type="text" name="last_name" id="last_name" />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="username">Username</label>
          <input v-model="create_acc_data.username" type="text" name="username" id="username" />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="password">Password</label>
          <input v-model="create_acc_data.password" type="text" name="password" id="password" />
        </div>
      </div>
      <div class="row">
        <div class="col">
          <label for="email">Email</label>
          <input v-model="create_acc_data.email" type="email" name="email" id="email" />
        </div>
      </div>

      <button @click="create_acc" class="btn btn-primary">Create Account</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      response_data: Object,
      create_acc_data: {
        first_name: "",
        last_name: "",
        username: "",
        password: "",
        email: "",
      },
    };
  },
  methods: {
    test_method: function () {
      console.log("THIS TEST METHOD WAS SUCCESFUL");
    },
    create_acc: function () {
      const post_url = "http://localhost:5000/api/createAccount";
      axios({
        method: "post",
        url: post_url,
        data: this.create_acc_data,
      }).then(
        (response) => {
          console.log(response);
          this.$emit("maybe_created", response);
        },
        (error) => {
          console.log(error);
        }
      );
    },
  },
};
</script>

<style>
</style>