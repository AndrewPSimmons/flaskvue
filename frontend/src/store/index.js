import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        loggedin: false,
        state_m: "IM THE STATE",
        logged_user: ""
    },
    mutations: {
        login(state) {
            state.loggedin = true;
        },
        logout(state) {
            state.loggedin = false;
        },
        change_logged_user(state, user) {
            state.logged_user = user
        }
    },
    actions: {
        update_loggedin_status(context) {
            const path = "http://localhost:5000/api/loggedin";
            axios
                .get(path)
                .then((response) => {
                    var status = response.data.loggedin;
                    console.log("HERE IS THE STATUS", status)
                    if (status == true) {
                        context.commit('login')
                    } else if (status == false) {
                        context.commit('logout')
                    }
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        get_logged_user(context) {
            axios({
                method: "get",
                url: "http://localhost:5000/api/loggedUser",
            }).then((response) => {
                context.commit('change_logged_user', response.data)
            });
        }
    },
    getters: {
        is_logged_in(state) {
            return state.loggedin;
        },
        logged_user(state) {
            return state.logged_user;
        }
    }
})