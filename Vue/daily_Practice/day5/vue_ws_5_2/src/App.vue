

<template>
<div>
    <header>
    <div class="header-box">
        <h1>명함 관리 페이지</h1>
    </div>
    <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </header>

    <main>

    </main>

    <article>
        <BusinessCard />
    </article>

    <footer>
    <div class="footer-box">
        <p>© 2023 My Business Cards</p>
    </div>
    </footer>
</div>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue'

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

}

.footer-box {
    background-color: #ccc; /* 회색 배경 */
    text-align: center;
    padding: 10px;
    position: fixed;
    bottom: 0;
    width: 100%;
}

h1, h2 {
    font-size: 24px;
}
</style>
