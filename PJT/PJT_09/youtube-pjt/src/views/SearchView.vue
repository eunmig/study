<template>
    <div>
        <div class="back" @click="moveBack">
            <i class="bi bi-arrow-left fs-3">뒤로가기</i>
        </div>
        <h1>비디오 검색</h1>
        <SearchForm 
            @input-keyword ="searchVideo"
        />
        <div class="video-list">
            <VideoCard 
                v-for="video in videos" :key="video.etag"
                :video="video"
            />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import SearchForm from '../components/SearchForm.vue';
import { RouterLink, useRouter } from 'vue-router';
import axios from 'axios'
import VideoCard from '@/components/VideoCard.vue'

const key = import.meta.env.VITE_YOUTUBE_KEY
const videos = ref([])

const router = useRouter()
const moveBack = function() {
    router.push({
        name:'home'
    })
}

// const saveData = function (data) {
//     // localstorage에 videos.value 저장
//     const jsonData = JSON.stringify(data)
//     console.log(jsonData)
//     localStorage.setItem('youtube-videos', jsonData)
// } 

// const loadData = function () {
//     const jsonData = localStorage.getItem('youtube-videos')
//     return JSON.parse(jsonData)
// }

// onMounted(() => {
//     videos.value = loadData()
//     // console.log(videos.value)
// })

const searchVideo = function(keyword) {
    const url = 'https://www.googleapis.com/youtube/v3/search'
    const params = {
        key,
        part: 'snippet',
        q: keyword,
        type: 'video'
    }
    axios({
        method: 'get',
        url,
        params,
    })
        .then(res=>{
            videos.value = res.data.items
            // saveData(videos.value)
        })
        .catch(err => {

        })
}   
</script>

<style scoped>
.back:hover {
    cursor: pointer;
}
.back i {
    font-style: normal;
}
.back {
    width: 140px;
    margin: 20px 0;
    background-color: #f6f6f6;
}
.video-list {
    display: flex;
    flex-wrap: wrap;
}
</style>