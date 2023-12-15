<template>
    <q-header reveal class="navbar bg-secondary">
        <q-toolbar class="q-container bg-transparent q-pa-md">
            <q-toolbar-title class="navbar__title"> ROBO.SCHOOL </q-toolbar-title>
            <a id="nav1" class="navbar__link" href="#school"> О школе </a>
            <a id="nav2" class="navbar__link" href="#teachers"> Тренеры </a>
            <a id="nav3" class="navbar__link" href="#price"> Стоимость </a>
            <q-toolbar-title id="nav4"  class="navbar__phone"> +7 800 000 11 22 </q-toolbar-title>
            
            <img src="../assets/images/phone.png"  class="navbar__menu-btn" alt="" @click="dialog = true">
            <img src="../assets/images/menu.png"  class="navbar__menu-btn" alt="" @click="dialog = true">
        </q-toolbar>

        <q-dialog v-model="dialog" class="modal">
            <img src="../assets/images/close1.png"  class="modal__btn" alt="" @click="dialog = false">
            <div class="col">
            <h4 class="modal__link" href="#school" @click="dialog = false">О школе</h4>
            <h4 class="modal__link" href="#teachers" @click="dialog = false">Тренеры</h4>
            <h4 class="modal__link" href="#price" @click="dialog = false">Стоимость</h4>
        </div>
        </q-dialog>
    </q-header>
</template>
<script setup lang="ts">
import { ref } from 'vue';

var dialog = ref(false)
</script>