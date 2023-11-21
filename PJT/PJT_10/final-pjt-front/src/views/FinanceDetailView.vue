<template>
  <button @click="fetchData">새로고침</button>
  <div>
    <h1>{{ item?.fin_prdt_nm }}</h1>
    <p>{{ item?.kor_co_nm }}</p>
    <p v-html="formattedEtcNote"></p>
    <OptionList :options="itemOption" />
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useFinanceStore } from '../stores/finance';
import { useAuthStore } from '../stores/auth';
import OptionList from '../components/OptionList.vue';

const authStore = useAuthStore();
const token = authStore.token;
const financeStore = useFinanceStore();
const route = useRoute();
const router = useRouter();
const itemOption = ref([]);
const item = ref(null);
console.log('item', item)

const formattedEtcNote = computed(() => {
  return item.value?.etc_note ? item.value.etc_note.replace(/\n/g, '<br>') : '';
});

const fetchData = async () => {
  try {
    const optionsResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product-options/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    });
    itemOption.value = optionsResponse.data;
    console.log('상품 옵션 res', optionsResponse.data);

    const productResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    });
    item.value = productResponse.data;
    console.log('금융상품 res', productResponse.data);
  } catch (error) {
    console.error(error);
  }
};

const beforeEach = async (to, from, next) => {
  // Check if the route has the necessary parameter (assuming id is required)
  if (to.params.id) {
    // Fetch data before navigating to the route
    await fetchData();
  }
  next();
};

// Expose the function to the component options
{ beforeEach }
</script>


<style scoped>

</style>