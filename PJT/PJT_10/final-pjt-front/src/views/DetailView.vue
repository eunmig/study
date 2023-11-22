<template>
  <div>
    <h1>게시글 상세 정보</h1>
    <div v-if="post">
      <p>{{ post.category.name }}</p>
      <p>{{ post.id }}번 글</p>
      <h3>{{ post.title }}</h3>
      <hr>
      <p>{{ post.created_at }}</p>
      <p>{{ post.updated_at }}</p>
      <hr>
      <p>{{ post.content }}</p>
      <div v-if="post.user === userData.id">
      <button @click="deletePost">삭제</button>
      <RouterLink :to="{ name: 'EditPost', params: { post_pk: post_pk } }">수정</RouterLink> 
      
      </div>
      <hr>
      <div>
        <h2>댓글</h2>
        <form @submit.prevent="createComment">
          <label for="comment">댓글</label>
          <input type="text" id="content" v-model.trim="content">
          <button type="submit">댓글 작성</button>
        </form>
        <ul>
          <li v-for="comment in post.comment_set" :key="comment.id">
            {{ comment.id }}번 댓글: {{ comment.content }}
            {{ comment.user }}
            <div>
            <button @click="deleteComment(comment.id)">삭제</button>
            <button @click="showEditForm(comment)">수정</button>
            </div>
          </li>
        </ul>
      </div>
      <hr>
    </div>
    <div v-else>Loading</div>
    <div class="modal" v-show="showEditModal">
      <form @submit.prevent="editComment">
        <label for="editedContent">Edit Comment:</label>
        <input type="text" id="editedContent" v-model.trim="editedContent">
        <button type="submit">Save</button>
      </form>
    </div>
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
    router.push({ name:'Post' })
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
</script>

<style scoped>
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 20px;
  z-index: 1000;
  display: none; /* Hidden by default */
}
</style>
