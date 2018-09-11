
(function() {
  "use strict";

  Vue.filter("date", (value) => {
    return value ? new Date(value).toLocaleString() : ""
  })

  var app = new Vue({

    el: "#app",

    data: {
      errors: {},
      tweet: {},
      tweets: [],
    },

    mounted() {
      this.loadTweets()
    },

    methods: {
      checkForm() {
        this.$set(this.errors, "name", null)
        this.$set(this.errors, "message", null)
        const request = {
          method: "POST",
          headers: {"Content-Type": "application/json; charset=utf-8"},
          body: JSON.stringify(this.tweet),
        }
        fetch("/api/v1/tweets/", request).then(response => {
          response.json().then(data => {
            if (response.ok) {
              this.tweets.push(data)
              this.tweet = {}
            }
            else {
              this.errors = Object.assign({}, this.errors, data)
            }
          })
        })
      },
      loadTweets() {
        fetch("/api/v1/tweets/").then(response => {
          if (response.ok) {
            response.json().then(data => {
              this.tweets = data
              this.$set(this.errors, "tweets", null)
            })
          }
          else {
            this.errors = Object.assign({}, this.errors, {tweets: response.statusText})
          }
        })
      }
    }

  })

})();
