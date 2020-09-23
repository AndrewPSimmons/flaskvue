<template>
  <div>
    <nav class="navbar navbar-expand-md">
      <a class="navbar-brand" href="/">Logo</a>
      <button
        class="navbar-toggler navbar-dark"
        type="button"
        data-toggle="collapse"
        data-target="#main-navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="main-navigation">
        <ul class="navbar-nav">
          <li class="nav-item" v-for="tag in tag_name_list" :key="tag.tag">
            <nav-tag :tag_info="tag"></nav-tag>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import axios from "axios";
import store from "../store/index";
import NavTag from "./NavTag";
export default {
  components: {
    NavTag,
  },
  data() {
    return {
      logged_user: String,
    };
  },
  computed: {
    tag_name_list: function () {
      if (store.getters.is_logged_in == false) {
        this.tag_names = [
          { text: "Home", source: "/" },
          { text: "About", source: "/about" },
          { text: "Login", source: "/login" },
        ];
      } else {
        this.tag_names = [
          { text: "Home", source: "/" },
          { text: "About", source: "/about" },
          { text: "Account", source: "/account" },
        ];
      }
      return this.tag_names;
    },
  },
};
</script>

<style scoped>
body {
  padding: 0;
  margin: 0;
  background: #f2f6e9;
}
/*--- navigation bar ---*/
.navbar {
  background: #3e7bff;
}
.nav-link,
.navbar-brand {
  color: #fff;
  cursor: pointer;
}
.nav-link {
  margin-right: 1em !important;
}
.navbar-collapse {
  justify-content: flex-end;
}
a {
  color: #fff;
}
</style>