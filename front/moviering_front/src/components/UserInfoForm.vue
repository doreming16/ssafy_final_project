<template>
  <div>
    <form>
        <!-- 성별 / 연령대 / 선호하는 영화 장르 / 관람시 중요한 요소 / 생일 -->
      <p>
        <label for="gender" class="form_label">성별</label>
        <input type="radio" name="gender" value="male" id="user_gender" />남성
        <input type="radio" name="gender" value="female" id="user_gender" />여성
      </p>
      <p>
        <!-- 연령대 .. 이 서비스를 12-19세도 많이 이용할까? -->
        <label for="age" class="form_label">연령대</label>
        <input type="radio" name="age" id="age" value="under_twelve"/>12세 이하
        <input type="radio" name="age" id="age" value="twelve"/>12세
        <input type="radio" name="age" id="age" value="fifteen"/>15세
        <input type="radio" name="age" id="age" value="over_nineteen"/>19세 이상
      </p>
      <p>
        <span for="user_name" class="form_label">선호하는 영화 장르 </span>
        <div>
          <!-- 장르 json에 맞춰서 직접 넣을까 ? -->
          <!-- json file for 돌리면서 할 수 있는 방법 없나? -->
            <input type="button" value="SF/판타지" name="favorite_genre" class="fav_genre_button" />
            <input type="button" value="로맨스" name="favorite_genre" class="fav_genre_button" />
            <input type="button" value="스릴러" name="favorite_genre" class="fav_genre_button" />
            <input type="button" value="드라마/가족" name="favorite_genre" class="fav_genre_button" />
            <input type="button" value="등등" name="favorite_genre" class="fav_genre_button" />
        </div>
      </p>
      <p>
        <!-- 연령대 .. 이 서비스를 12-19세도 많이 이용할까? -->
        <span for="viewing_environment" class="form_label">영화 관람 시 나에게 중요한 요소</span>
        <div>
          <input type="radio" name="viewing_environment" id="viewing_environment" value="accessibility"/>접근성
          <input type="radio" name="viewing_environment" id="viewing_environment" value="sound"/>음향
          <input type="radio" name="viewing_environment" id="viewing_environment" value="screen_width"/>화면 크기
          <input type="radio" name="viewing_environment" id="viewing_environment" value="etc"/>기타
        </div>
      </p>
      <p>
        <label for="birthday" class="form_label">생일</label>
        <input type="" name="birthday" id="birthday">
      </p>
      <input type="submit" value="정보 등록" id="submit_info_button">
    </form>
  </div>
</template>

<script setup></script>

<style scoped>
h3 {
  color: green;
}
.form_label{
  color: pink;
  margin-right: 10px;
}
.fav_genre_button{
  border-radius: 20px;
padding: 4px 10px;
margin: 5px;
}
#submit_info_button{
  padding: 5px 10px;
}
</style>
