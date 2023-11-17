<template>
    <div class="card-wrapper">
        <div class="card h-100">
            <img @click="movedetail" :src="thumbnailUrl" class="card-img-top" alt="...">
            <div class="card-body">
                <h6 class="card-title">{{ videoTitle }}</h6>
            </div>
        </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
    video: Object,
})

const thumbnailUrl = computed(() => props.video.snippet.thumbnails.medium.url)
const videoTitle = computed(() => props.video.snippet.title)
const videoId = computed(() => props.video.id.videoId)
const description = computed(() => props.video.snippet.description)

const router = useRouter()
const movedetail = function () {
    router.push({
        name: 'detail',
        params: { id: videoId.value },
        query: {
            videoData: JSON.stringify(props.video)
        }
    })
}
</script>

<style scoped>
.card-wrapper {
    width: 300px;
    height: 300px;
    margin: 1rem;
}
</style>
