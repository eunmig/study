<template>
    <div>
        <header>
        <div class="header-box">
            <h1>명함 관리 페이지</h1>
        </div>
        <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
        <div>
            <CreateCardForm @createCardEvent="addBusinessCard" :newCard="newCard" />
        </div>
        </header>
    
        <main>
        </main>
    
        <article>
            <BusinessCard :newCard="newCard" />
        </article>
    </div>

    <footer class="footer-box">
        <p>© 2023 My Business Cards</p>
    </footer>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue'
import CreateCardForm from '@/components/CreateCardForm.vue';
import { ref } from 'vue'

const businessCards = ref([])
const newCard = ref(null)

const addBusinessCard = (cardInfo) => {
  // 이미 존재하는 명함인지 중복 검사
  if (!businessCards.value.some((card) => card.name === cardInfo.name)) {
    businessCards.value.push(cardInfo)
  }

  newCard.value = cardInfo
}
</script>

<style scoped>
header, main, article, footer {
    display: flex;
    justify-content: center;
    align-items: center;
    /* min-height: 100vh; */
    flex-direction: column;
}

.header-box,
.main-box {
    background-color: #3498db; /* 파란색 배경 */
    text-align: center;
    padding: 20px;
    border-radius: 10px;
    margin: 20px;
}

.article-box {
    background-color: #ccc; /* 회색 배경 */
    text-align: center;
    padding: 20px;
    border-radius: 10px;
    margin: 20px;
    overflow-y: scroll;
}

.footer-box {
    background-color: #ccc; /* 회색 배경 */
    text-align: center;
    padding: 10px;
    position: flex;
    bottom: 0px;
    width: 100%;
}

h1, h2 {
    font-size: 24px;
}

</style>
