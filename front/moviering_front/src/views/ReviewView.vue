<template>


<div class="row2">
  <p id="question">이 영화, 어떠셨나요?</p>   
</div>

<div>
    <form @submit.prevent="createReview">
      <div>
        <label for="rating">평점 : </label>
        <input type="text" v-model.trim="rating" id="rating">
      </div>
      <div>
        <label for="content">감상평 : </label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit" value="작성">
    </form>
</div>

<div>
  <div
    v-for="review in reviews"
    :key="review.id"
    :review="review"
  >
    {{ review.rating }}
    {{ review.content }}
    <br>
  </div>
</div>

</template>
  
<script setup>
import axios from 'axios'

import { onMounted, ref, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const rating = ref(null)
const content = ref(null)
const router = useRouter()

const props = defineProps({
  id: Number
})


// Read
onMounted(() => {
    store.getReviews(props.id)
})
const reviews = ref(store.reviews)
console.log(reviews.value)

const createReview = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/detail/${props.id}/reviews/`,
    data: {
      rating: rating.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
    .then((response) => {
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style scoped>
.container .row1 {
    font-family: SUITE;
    display: flex;
    justify-content: center;
    margin: 50px 0px;
  }
  img {
    height: 500px;
  }
  #center_line {
    margin: 0px 50px;
    width: 0.5px;
    height: 500px;
    background-color: white;
  }
  .box_right {
    font-family: SUITE;
    width: 500px;
  }
  .list_name {
    font-weight: bold;
  }
  #movie_title {
    font-size: 30px;
  }
  #question {
    font-size: 25px;
    color: rgb(255, 204, 204);
  }
  .row2 {
    font-family: SUITE;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 50px 0px;
  }
  .count_stars {
    display: flex;
  }
  .star {
    width: 20px;
    height: 20px;
    margin: 5px;
  }
  .comment {
    width: 800px;
    height: 200px;
    background-color: transparent;
    border: 1px solid skyblue;
  }
  .row3 {
    display: flex;
    justify-content: center;
  }
  .submit_button {
    margin: 20px;
    width: 40px;
    height: 25px;
  }
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .title_comment {
    display: flex;
  }
  .box_comment {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px 0px;
  }
  .star_comment {
    width: 10px;
    height: 10px;
  }
  .user_comment {
    margin: 0px 10px;
  }
</style>