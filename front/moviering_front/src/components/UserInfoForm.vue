<template>
  <div>
    <form style="padding: 50px;">
        <!-- 성별 / 연령대 / 선호하는 영화 장르 / 관람시 중요한 요소 / 생일 -->

      <div>
        <label for="gender" class="form_label">성별</label>
        <div class="form_content">
          <input type="radio" name="gender" value="male" id="gendeR_male" v-model="gender"/>
          <label for="gender_male">
              남성
            </label>
          <input type="radio" name="gender" value="female" id="gender_female" v-model="gender"/>
      
          <label for="gender_female">
            여성
            </label>
        </div>
        <p style="color:green;">{{ gender }}</p>
      </div>


      <div>
        <label for="age" class="form_label">선호하는 영화 개봉 시기</label>
        <div class="form_content" style="display: flex; flex-direction:column;">
          <p>
            <input type="radio" name="age" id="bf1970" value="bf1970" v-model="age"/>
            <label for="bf1970">
              1970년대 이전
            </label>
          </p>
          <p>
            <input type="radio" name="age" id="1970s" value="1970s" v-model="age"/>
            <label for="1970s">
              1970년대
            </label>
          </p>
          <p>
            <input type="radio" name="age" id="1980s" value="1980s" v-model="age"/>
            <label for="1980s">
              1980년대
            </label>
          </p>
          <p>
            <input type="radio" name="age" id="1990s" value="1990s" v-model="age"/>
            <label for="1990s">
              1990년대
            </label>
          </p>
          <p>
            <input type="radio" name="age" id="2000s" value="2000s" v-model="age"/>
            <label for="2000s">
              2000년대
            </label>
          </p>
          <p>
            <input type="radio" name="age" id="2010s" value="2010s" v-model="age"/>
            <label for="2010s">
              2010년대
            </label>
          </p>
          <p>
            <input type="radio" name="age" id="af2020" value="af2020" v-model="age"/>
            <label for="af2020">
              2020년 이후
            </label>
          </p>
        </div>
        <p style="color:green;">{{ age }}</p>
      </div>


      <div>
        <label class="form_label">선호하는 영화 장르</label>
        <div style="display:flex; justify-content: center;">
          <div class="form_content form_genre_list">
            <div v-for="genre in data" style="margin: 10px;">
              <input type="checkbox" :value="genre.fields.name" :id="genre.fields.name" v-model="favorite_genre">
              <label :for="genre.fields.name">{{ genre.fields.name }}</label>
            </div>
          </div>
        </div>
        <p style="color:green;">{{ favorite_genre }}</p>
      </div>


      <div>
        <!-- 연령대 .. 이 서비스를 12-19세도 많이 이용할까? -->
        <span for="viewing_environment" class="form_label">영화 관람 시 나에게 중요한 요소</span>
        <div class="form_content" style="column-gap: 10px;">
          <p>
            <input type="radio" v-model="viewing_environment" id="accessibility" value="accessibility"/>
            <label for="accessibility">
              접근성
            </label>
          </p>
          <p>
            <input type="radio" v-model="viewing_environment" id="sound" value="sound"/>
            <label for="sound">
              음향
            </label>
          </p>
          <p>
            <input type="radio" v-model="viewing_environment" id="screen_width" value="screen_width"/>
            <label for="screen_width">
              화면 크기
            </label>
          </p>
          <p>
            <input type="radio" v-model="viewing_environment" id="etc" value="etc"/>
            <label for="etc">
              기타
            </label>
          </p>
        </div>
        <p style="color:green;">{{ viewing_environment }}</p>
      </div>


      <div>
        <label for="birthday_input" class="form_label">생일</label>
          <div>
            <input type="date" value="1997-05-10" name="birthday_input" id="birthday_input">
          </div>
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
#birthday_input{
  margin: 20px;
}
</style>
