<template>
  <div>
    <form>
        <!-- 성별 / 연령대 / 선호하는 영화 장르 / 관람시 중요한 요소 / 생일 -->

      <div>
        <label for="gender" class="form_label">성별</label>
        <div class="form_content">
          <input type="radio" name="gender" value="male" id="user_gender" v-model="gender"/>남성
          <input type="radio" name="gender" value="female" id="user_gender" v-model="gender"/>여성
        </div>
        <p style="color:green;">{{ gender }}</p>
      </div>


      <div>
        <label for="age" class="form_label">선호하는 영화 개봉 시기</label>
        <div class="form_content">
          <input type="radio" name="age" id="age" value="under_twelve" v-model="age"/>1970년대 이전
          <input type="radio" name="age" id="age" value="twelve" v-model="age"/>1970년대
          <input type="radio" name="age" id="age" value="fifteen" v-model="age"/>1980년대
          <input type="radio" name="age" id="age" value="over_nineteen" v-model="age"/>1990년대
          <input type="radio" name="age" id="age" value="over_nineteen" v-model="age"/>2000년대
          <input type="radio" name="age" id="age" value="over_nineteen" v-model="age"/>2010년대
          <input type="radio" name="age" id="age" value="over_nineteen" v-model="age"/>2020년 이후
        </div>
        <p style="color:green;">{{ age }}</p>
      </div>


      <div>
        <label class="form_label">선호하는 영화 장르</label>
        <div style="display:flex; justify-content: center;">
          <div class="form_content form_genre_list">
            <div v-for="genre in data" style="margin: 10px;">
              <input type="checkbox" :value="genre.fields.name" v-model="favorite_genre">
              <span>{{ genre.fields.name }}</span>
            </div>
          </div>
        </div>
        <p style="color:green;">{{ favorite_genre }}</p>
      </div>


      <div>
        <!-- 연령대 .. 이 서비스를 12-19세도 많이 이용할까? -->
        <span for="viewing_environment" class="form_label">영화 관람 시 나에게 중요한 요소</span>
        <div class="form_content">
          <input type="radio" v-model="viewing_environment" id="viewing_environment" value="accessibility"/>접근성
          <input type="radio" v-model="viewing_environment" id="viewing_environment" value="sound"/>음향
          <input type="radio" v-model="viewing_environment" id="viewing_environment" value="screen_width"/>화면 크기
          <input type="radio" v-model="viewing_environment" id="viewing_environment" value="etc"/>기타
        </div>
        <p style="color:green;">{{ viewing_environment }}</p>
      </div>


      <div>
        <label for="birthday" class="form_label">생일
          <div>
            <input type="date" value="1997-05-10" name="birthday" id="birthday">
          </div>
      </label>
    </div>
      <input type="submit" value="정보 등록" id="submit_info_button">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import data from '@/fixtures/genres.json'

const gender = ref('')
const age = ref('')
const favorite_genre = ref([])
const viewing_environment = ref(null)
const birthday = ref(null)

</script>

<style scoped>
h3 {
  color: green;
}
.form_label{
  color: pink;
  margin: 10px;
  font-weight: bold;
}
.form_content{
  font-weight: lighter;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 15px;
}
.fav_genre_button{
  font-family: SUITE;
  border-radius: 20px;
  border: none;
  padding: 4px 10px;
  margin: 5px;
}
.form_genre_list{
  width: 400px;
  display: flex;
  flex-wrap: wrap;
}
#submit_info_button{
  font-family: SUITE;
  padding: 5px 10px;
}
</style>
