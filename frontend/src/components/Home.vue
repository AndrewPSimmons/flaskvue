/* eslist-disable */

<template>
  <div>
    <nav-bar style="text-align: center;"></nav-bar>

    <section class="fdb-block hero-bg" id="formSection" style="min-height: 600px;">
      <div class="container" id="form">
        <div class="row justify-content-center">
          <div class="col-12 text-center">
            <div id="score header">OUTSIDE TEXT HERE</div>
          </div>
          <div class="row justify-content-center">
            <div class="col-12 col-lg-12 col-md-8 text-center">
              <div id="formOnly" class="promo-header__form-border form-box">
                PUT CONTENT HERE
                <p>Home page</p>
                <p>Random Number from backend: {{ randomNumber }}</p>
                <button @click="getRandom">New Random Number</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "./NavBar.vue";
export default {
  data() {
    return {
      randomNumber: 0,
    };
  },
  components: {
    NavBar,
  },
  methods: {
    getRandom() {
      this.randomNumber = this.getRandomFromBackend();
    },
    getRandomFromBackend() {
      const path = "http://localhost:5000/api/random";
      axios
        .get(path)
        .then((respnse) => {
          this.randomNumber = respnse.data.randomNumber;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getRandom();
  },
};
</script>

<style>
</style>
