import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
// BootstrapVue 3
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'


<<<<<<< HEAD
const app = createApp(App)
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)


// BootstrapVue 3 사용
app.use(BootstrapVue3)


// app.use(createPinia())
app.use(router)
app.use(pinia)

app.mount('#app')
=======

// BootstrapVue 3
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)

// BootstrapVue 3 사용
app.use(BootstrapVue3)


app.use(createPinia())
app.use(router)

app.mount('#app')


>>>>>>> 5f1367ace20c3b6af39823011830c3433fb7eb1b
