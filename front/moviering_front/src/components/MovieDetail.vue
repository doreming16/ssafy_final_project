<template>
  <div class="container">
    <div class="row1">
      <div class="box_left">
        <img src="../img/movie4.jpeg" alt="detail_movie_image" />
      </div>
      <div id="center_line"></div>
      <div class="box_right">
        <p id="movie_title">조제, 호랑이 그리고 물고기들</p>
        <p>일본</p>
        <p><span>2020-12-25</span> 개봉</p>
        <p>16, 18, 10749</p>
        <p>출연진</p>
      </div>
    </div>

    <div class="row2">
      <p id="question">이 영화, 어떠셨나요?</p>
      <div class="count_stars">
        <div v-for="count in count_stars">
          <img class="star" src="../icons/star1.png" alt="icon_star" />
        </div>
      </div>
    </div>

    <div class="row3">
      <form>
        <input class="comment" type="text" />
        <input class="submit_button" type="submit" value="입력" />
      </form>
    </div>

    <div class="row4">
      <div v-for="count in count_stars" class="box_comment">
        <div class="title_comment">
          <div class="user_comment">user1</div>
          <div class="count_stars">
            <div v-for="count in count_stars">
              <img
                class="star_comment"
                src="../icons/star1.png"
                alt="icon_star"
              />
            </div>
          </div>
        </div>
        <div>show Comment here</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
const count_stars = ref(4);
</script>

<style scoped>
.container .row1 {
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
