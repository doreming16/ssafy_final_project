<template>
  <div>
    <form @submit.prevent="submitForm" style="padding: 50px;">

      <div>
        <label for="gender" class="form_label">오늘의 기념일 관련 영화를 추천받으시겠습니까?</label>
        <div class="form_content">
          <input type="radio" name="isSpecial" value="True" id="isSpecial_true" v-model="formData.isSpecial"/>
          <label for="isSpecial_true">예</label>
          <input type="radio" name="isSpecial" value="False" id="isSpecial_false" v-model="formData.isSpecial"/>
          <label for="isSpecial_false">아니요</label>
        </div>
        <p style="color:green;">{{ formData.isSpecial }}</p>
      </div>

      <div class="form_divide" style="margin: 30px 0px;">
        -------------------------------------------------------------------------------
      </div>

      <div>
        <label for="gender" class="form_label">성별</label>
        <div class="form_content">
          <input type="radio" name="gender" value="male" id="gender_male" v-model="formData.gender"/>
          <label for="gender_male">
            남성
            </label>
          <input type="radio" name="gender" value="female" id="gender_female" v-model="formData.gender"/>
          <label for="gender_female">
            여성
            </label>
        </div>
        <p style="color:green;">{{ formData.gender }}</p>
      </div>

      <div class="form_divide" style="margin: 30px 0px;">
        -------------------------------------------------------------------------------
      </div>
      
      <div>
        <label class="form_label">선호하는 영화 개봉 시기</label>
        <div class="form_content" style="display: flex; flex-direction:column;">
          <p>
            <input type="radio" name="era" id="bf1970" value="bf1970" v-model="formData.era"/>
            <label for="bf1970">1970년대 이전</label>
          </p>
          <p>
            <input type="radio" name="era" id="1970s" value="1970s" v-model="formData.era"/>
            <label for="1970s">1970년대</label>
          </p>
          <p>
            <input type="radio" name="era" id="1980s" value="1980s" v-model="formData.era"/>
            <label for="1980s">1980년대</label>
          </p>
          <p>
            <input type="radio" name="era" id="1990s" value="1990s" v-model="formData.era"/>
            <label for="1990s">1990년대</label>
          </p>
          <p>
            <input type="radio" name="era" id="2000s" value="2000s" v-model="formData.era"/>
            <label for="2000s">2000년대</label>
          </p>
          <p>
            <input type="radio" name="era" id="2010s" value="2010s" v-model="formData.era"/>
            <label for="2010s">2010년대</label>
          </p>
          <p>
            <input type="radio" name="era" id="af2020" value="af2020" v-model="formData.era"/>
            <label for="af2020">2020년 이후</label>
          </p>
        </div>
        <p style="color:green;">{{ formData.era }}</p>
      </div>

      <div class="form_divide" style="margin: 30px 0px;">
        -------------------------------------------------------------------------------
      </div>

      <div>
        <label class="form_label">선호하는 영화 장르</label>
        <div style="display:flex; justify-content: center;">
          <div class="form_content form_genre_list">
            <div v-for="genre in data" style="margin: 10px;">
              <input type="checkbox" :value="genre.pk" :id="genre.fields.name" v-model="formData.favorite_genre">
              <label :for="genre.fields.name">{{ genre.fields.name }}</label>
            </div>
          </div>
        </div>
        <p style="color:green;">{{ formData.favorite_genre }}</p>
      </div>

      <div class="form_divide" style="margin: 30px 0px;">
        -------------------------------------------------------------------------------
      </div>

      <div>
        <span for="viewing_environment" class="form_label">영화 관람 시 나에게 중요한 요소</span>
        <div class="form_content" style="column-gap: 10px;">
          <p>
            <input type="radio" v-model="formData.viewing_environment" id="accessibility" value="accessibility"/>
            <label for="accessibility">접근성</label>
          </p>
          <p>
            <input type="radio" v-model="formData.viewing_environment" id="sound" value="sound"/>
            <label for="sound">음향</label>
          </p>
          <p>
            <input type="radio" v-model="formData.viewing_environment" id="screen_width" value="screen_width"/>
            <label for="screen_width">화면 크기</label>
          </p>
          <p>
            <input type="radio" v-model="formData.viewing_environment" id="etc" value="etc"/>
            <label for="etc">고려하지 않음</label>
          </p>
        </div>
        <p style="color:green;">{{ formData.viewing_environment }}</p>
      </div>

      <div class="form_divide" style="margin: 30px 0px;">
        -------------------------------------------------------------------------------
      </div>
      
      <div>
        <label for="birthday_input" class="form_label">생일</label>
          <div>
            <input type="date" v-model="formData.birthday" value="1997-05-10" name="birthday_input" id="birthday_input">
          </div>
          <p style="color:green;">{{ formData.birthday }}</p>
    </div>
      <input type="submit" value="정보 등록" id="submit_info_button">

      <!-- <div>
        <span v-for="genre in data" style="margin: 10px;">
          <label :for="genre.fields.name">{{ genre.fields.name }}</label>
        </span>
      </div> -->

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import data from '@/fixtures/genres.json';
import axios from 'axios';


const formData  = ref({
  isSpecial: undefined,
  gender: '',
  era: '',
  favorite_genre: [],
  viewing_environment: '',
  birthday: null
});

const submitForm = () => {
    console.log(formData.value)
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/api/submit-form/',
      data: formData.value,
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(res => {
      console.log(res.data)
    }).catch(err => {
      console.log(err)
    })
  };

</script>

<style scoped>
h3 {
  color: green;
}
.form_label{
  color: pink;
  font-size: 20px;
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
.form_divide{
  margin: 30px;
}

#submit_info_button{
  font-family: SUITE;
  font-size: 13px;
  padding: 6px 10px;
  color: white;
  border: 3px solid pink;
  background-color: transparent;
  margin: 50px;
  cursor: pointer;
}
</style>
