<template>
  <div class="post-detail-container">
    <div class="two alt-two">
        <h1>게시글 상세 정보
            <span>   </span>
        </h1>
        <br>
    </div>
    
    <div v-if="post">
      <div class="post-meta">
        <div style="display: flex; justify-content: center; column-gap: 10px;">
          <div style="flex: 1; text-align: left;">
            <p class="category">{{ post.category.name }}</p>
            <h3>{{ post.title }}</h3>
          </div>
          <div style="flex: 1; text-align: right;">
            <p class="date" style="text-align: right">작성일: {{ formatDate(post.created_at) }}</p>
            <p class="date" style="text-align: right">수정일: {{ formatDate(post.updated_at) }}</p>
            <p style="text-align: right">작성자: {{ post.user_data.username }}</p>
          </div>
        </div>
        <hr>
        <div class="post-content">
          <p>{{ post.content }}</p>
        </div>
      </div>

      <div v-if="post.user === userData.id" class="post-actions">
        <button @click="deletePost" class="delete-btn">게시글 삭제</button>
        <RouterLink :to="{ name: 'EditPost', params: { post_pk: post_pk } }" class="edit-link">게시글 수정</RouterLink>
      </div>

      <hr>

      <div class="comments-section">
        <h2>Comments</h2>

        <form @submit.prevent="createComment" class="comment-form">
          <input type="text" id="content" v-model.trim="content" placeholder="댓글을 입력하세요" class="comment-input">
          <button type="submit" class="comment-btn">댓글 작성</button>
        </form>

        <ul class="comment-list">
          <li v-for="comment in post.comment_set" :key="comment.id" class="comment-item">
            <div class="comment-content">
              <p class="comment-id">번호 : {{ comment.id }}번 댓글</p>
              <p class="comment-text">댓글 내용 : {{ comment.content }}</p>
              <p class="comment-user">작성자: {{ comment.user }}</p>
            </div>

            <div v-if="comment.user === userData.id" class="comment-actions">
              <button @click="deleteComment(comment.id)" class="delete-btn">댓글 삭제</button>
              <button @click="showEditForm(comment)" class="edit-btn">댓글 수정</button>
            </div>
            <div v-show="showEditModal">
              <form @submit.prevent="editComment">
                <label for="editedContent">댓글 수정:</label>
                <input type="text" id="editedContent" v-model.trim="editedContent" class="edit-input">
                <button type="submit" class="edit-btn">저장</button>
              </form>
            </div>
          </li>
        </ul>
      </div>
    <hr>
    </div>

    <div v-else>Loading</div>


  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, } from 'vue-router'
import { useCommunityStore } from '../stores/community'
import { useAuthStore } from '../stores/auth'
import router from '../router'
import { RouterLink } from 'vue-router'

const authStore = useAuthStore()
const token = authStore.token
const store = useCommunityStore()
const route = useRoute()
const post = ref(null)
const content = ref(null)
const userData = authStore.userData
const post_pk = route.params.id

console.log('dtaa', userData.id)
// 댓글 수정용
const showEditModal = ref(false)
const editedContent = ref(null)
const editCommentId = ref(null)

const showEditForm = function(comment) {
  editCommentId.value = comment.id
  editedContent.value = comment.content
  showEditModal.value = true
  console.log('clicked', showEditModal.value)
  console.log(editCommentId.value, editedContent.value)
}


const editComment = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/community/comments/${editCommentId.value}/`,
    data: {
      content: editedContent.value
    }
  }).then((res) => {
    console.log(editedContent.value)

    const editedCommentIndex = post.value.comment_set.findIndex(comment => comment.id === editCommentId.value)

    if (editedCommentIndex !== -1) {
      post.value.comment_set.splice(editedCommentIndex, 1, res.data)
    }

    editedContent.value = ''
    showEditModal.value = false  // Close the modal after editing
  }).catch(err => console.error('Error editing comment:', err))
}


const createComment = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/community/posts/${route.params.id}/comment/`,
    headers: {
      Authorization: `Token ${token}`
    },
    data: {
      content: content.value
    }
  }).then((res) => {
    content.value = ''
    post.value.comment_set.push(res.data)
  }).catch(err => console.log(err))
}

const deleteComment = function (commentId) {
  axios({
    method: 'delete',
    url: `${store.API_URL}/community/comments/${commentId}/`
  })
  .then(() => {
    post.value.comment_set = post.value.comment_set.filter(comment => comment.id !== commentId);
    console.log('댓글 삭제 완료')
  })
  .catch(err => console.error('Error deleting comment:', err))
}

const deletePost = () => {
    console.log('포스트 삭제 완료')
    axios({
        method: 'delete',
        url: `${store.API_URL}/community/post_delete/${route.params.id}/`,
        headers: {
            Authorization: `Token ${token}`
        }
    }).then((res) => {
        // Remove the deleted post from local storage
        const communityData = JSON.parse(localStorage.getItem('community')) || { posts: [], categories: [] };

        // Filter out the deleted post
        communityData.posts = communityData.posts.filter(post => post.id !== route.params.id);

        // Update local storage
        localStorage.setItem('community', JSON.stringify(communityData));

        router.push({ name: 'Post' });
    })
}


onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/post/${route.params.id}/`,
    headers: {
      Authorization: `Token ${token}`
    }
  })
  .then((res) => {
    post.value = res.data
    console.log('detail res', res.data)
  })
  .catch(err => console.log(err))
})

const formatDate = (value) => {
  if (!value) return ""
  // Format the date to show only up to the minute
  return new Date(value).toLocaleString("kr", {
    year: "numeric",
    month: "numeric",
    day: "numeric",
    hour: "numeric",
    minute: "numeric",
  })
}
</script>

<style scoped>
@import "@/views/DetailView.scss"

</style>