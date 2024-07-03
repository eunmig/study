<template>
  <div class="two alt-two">
    <h1>{{ item?.fin_prdt_nm }}
        <span>{{ item?.kor_co_nm }}</span>
    </h1>
    <br>
  </div>
  <button class="btn btn-primary" @click="toggleLike">
    {{ isLiked ? '관심 상품 해제' : '관심 상품 등록' }}
  </button>
  <div>
    <table>
      <thead>
        <tr>
          <th colspan="2">상품명</th>
          <th colspan="2">은행명</th>
        </tr>
      </thead>
        <tr>
          <td colspan="2">{{ item?.fin_prdt_nm }}</td>
          <td colspan="2">{{ item?.kor_co_nm }}</td>
        </tr>

        <br>

      <thead>
        <tr>
          <th>상품설명</th>
          <th>우대대상</th>
          <th>가입방법</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td v-html="formattedEtcNote"></td>
          <td>{{ item?.join_member }}</td>
          <td>{{ item?.join_way }}</td>
        </tr>

        <br>

      <thead>
        <tr>
          <th>우대조건</th>
        </tr>
      </thead>
      <tr>
        <td v-html="formattedspclcnd" colspan="4"></td>
      </tr>

        <br>
        
        <tr>
          <td colspan="4">
            <!-- 추가된 행에 OptionList 컴포넌트 추가 -->
            <OptionList :options="itemOption" />
          </td>
        </tr>
      </tbody>
    </table>
    <br>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useFinanceStore } from '../stores/finance';
import { useAuthStore } from '../stores/auth';
import OptionList from '../components/OptionList.vue';

const authStore = useAuthStore();
const token = authStore.token;
const financeStore = useFinanceStore();
const route = useRoute();
const itemOption = ref([]);
const item = ref(null);
const isLiked = ref(false);

const formattedEtcNote = computed(() => {
  return item.value?.etc_note ? item.value.etc_note.replace(/\n/g, '<br>') : '';
});

const formattedspclcnd = computed(() => {
  return item.value?.spcl_cnd ? item.value.spcl_cnd.replace(/\n/g, '<br>') : '';
});


const fetchData = async () => {
  try {
    const optionsResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product-options/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    itemOption.value = optionsResponse.data;
    console.log('상품 옵션 res', optionsResponse.data);

    const productResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    item.value = productResponse.data;
    console.log('금융상품 res', productResponse.data);

    // Check if the current user has liked the product
    isLiked.value = productResponse.data.like_users.includes(authStore.userData.id);
  } catch (error) {
    console.error(error);
  }
}

const toggleLike = async () => {
  try {
    const likeResponse = await axios.post(
      `${financeStore.API_URL}/finance/likes/${item.value.fin_prdt_cd}/`,
      null,
      {
        headers: {
          Authorization: `Token ${token}`
        }
      }
    );
    
    // Update isLiked based on the server response
    isLiked.value = likeResponse.data.liked;

    // Show alert based on the like status
    const message = isLiked.value ? '관심 목록에 추가 되었습니다.' : '관심 목록에서 해제 되었습니다.'
    window.alert(message);
  } catch (error) {
    console.error('Error toggling like:', error)
  }
}


onMounted(() => {
  fetchData();
  console.log('onMount: FinanceDetailView');
});
</script>

<style scoped>
@import "@/views/FinanceDetailView.scss"

</style>
