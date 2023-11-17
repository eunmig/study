<template>
  <div>
    <h1>{{ videoData.snippet.title }}</h1>
    <div>
      <iframe id="ytplayer" type="text/html" width="640" height="360"
              :src="videoUrl"
              frameborder="0"></iframe>
    </div>
    <p>{{ videoData.snippet.description }}</p>
    <p>
      <button @click="addVideo(videoData)">나중에 볼 동영상에 추가</button>
    </p>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const videoId = ref(route.params.id)
const videoUrl = computed(() => `https://www.youtube.com/embed/${videoId.value}`)
const videoData = ref(JSON.parse(route.query.videoData || '{}'))

const addVideo = (video) => {
  // 현재 localStorage에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingVideos = JSON.parse(localStorage.getItem('youtube-videos')) || []

  // 중복된 데이터가 있는지 확인
  const isDuplicate = existingVideos.length > 0 && existingVideos.find((item) => item.id === video.id)

  // 중복이 아니라면 추가
  if (!isDuplicate) {
    alert('나중에 볼 동영상에 추가합니다');
    existingVideos.push(video);
  } else {
    alert('이미 있는 동영상입니다. 나중에 볼 동영상으로 이동합니다.')
  }

  // 수정된 데이터를 localStorage에 저장
  localStorage.setItem('youtube-videos', JSON.stringify(existingVideos))

  // 이동할 페이지 또는 추가적인 동작을 수행하려면 여기에서 처리
};
</script>

<style scoped>
/* Your styles go here */
</style>
