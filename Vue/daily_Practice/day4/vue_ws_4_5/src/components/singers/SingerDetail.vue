<template>
    <div class="card">
        <h1 class="singer-name">가수 이름</h1>
        <div class="singer-img">
            <div class="image-container">
                <img src="src/assets/singer.jpg" alt="가수이미지">
            </div>
        </div>
        <p class="singer-info">가수 소개글</p>

        <div class="album">
        <SingerAlbum /> 
        <SingerAlbum />
        </div>
  

    </div>
</template>

<script setup> 
import SingerAlbum from '@/components/singers/SingerAlbum.vue';

</script>

<style scoped>

/* 가수 이름, 가수 소개글 가운데 정렬 */
.singer-name, .singer-info {
    text-align: center;
}

/* 가수 이미지 가운데 정렬 */
.singer-img {
    display: flex;
    justify-content: center;
}

/* .singer-img 클래스 내부에 있는 .image-container 클래스를 선택하여 해당 요소에 스타일을 적용하는데 사용 */
/* 가수 이미지 원형 스타일 */
.singer-img .image-container {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
}

/* 이미지를 부모 요소의 크기에 맞춰 조정 */
.singer-img .image-container img {
    width: 100%;
    height: 100%;
}

.card {
    display: inline-block;
    width: 40%;
    margin: 20px;
    border: 1px solid;
}
.album {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>

<style>
h1 {
    color: green;
}
</style>