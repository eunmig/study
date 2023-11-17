<template>
    <div>
      <div class="back" @click="moveBack">
        <i class="bi bi-arrow-left fs-3">뒤로가기</i>
      </div>
      <h1>나중에 볼 동영상</h1>
      <div v-if="videoItems" class="card-wrapper">
        <div v-for="video in videoItems" :key="video.id" class="card h-100">
          <img :src="video.snippet.thumbnails.medium.url" class="card-img-top" alt="...">
          <div class="card-body">
            <h6 class="card-title">{{ video.snippet.title }}</h6>
            <button @click="removeVideo(video)">나중에 볼 동영상에서 삭제</button>
          </div>
        </div>
      </div>
      <div v-else>
        <strong>등록된 동영상 없음.</strong>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  
  const videoItems = ref(JSON.parse(localStorage.getItem('youtube-videos')) || []);
  
  const moveBack = () => {
    router.push({ name: 'home' });
  };
  
  const removeVideo = (video) => {
    // localStoage에서 삭제
    // 현재 videoItems.value에서 삭제
    const itemIdx = videoItems.value.findIndex((item) => item.id === video.id);
  
    if (itemIdx !== -1) {
      videoItems.value.splice(itemIdx, 1);
      localStorage.setItem('youtube-videos', JSON.stringify(videoItems.value));
    }
  };
  </script>
  