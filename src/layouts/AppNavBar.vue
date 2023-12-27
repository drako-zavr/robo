<template>
    <q-header reveal class="navbar bg-secondary">
        <q-toolbar class="q-container bg-transparent q-pa-md">
            <q-toolbar-title class="navbar__title"> ROBO.SCHOOL </q-toolbar-title>
            <a class="navbar__link" href="#school"> О школе </a>
            <a class="navbar__link" href="#teachers"> Тренеры </a>
            <a class="navbar__link" href="#price"> Стоимость </a>
            <q-toolbar-title class="navbar__phone"> +7 800 000 11 22 </q-toolbar-title>
            
            <img src="../assets/images/phone.png"  class="navbar__menu-btn" @click="dialog_phone = true">
            <img src="../assets/images/menu.png"  class="navbar__menu-btn" @click="dialog = true">
        </q-toolbar>

        <q-dialog v-model="dialog" class="modal">
            <img src="../assets/images/close.png"  class="modal__btn" @click="dialog = false">
            <div class="col">
            <p class="modal__link" href="#school" @click="dialog = false">О школе</p>
            <p class="modal__link" href="#teachers" @click="dialog = false">Тренеры</p>
            <p class="modal__link" href="#price" @click="dialog = false">Стоимость</p>
        </div>
        </q-dialog>
        <q-dialog v-model="dialog_phone" class="modal">
            <img src="../assets/images/close.png" class="modal__btn" @click="dialog_phone = false">
            <div class="col">
            <p class="modal__link" href="#school" @click="dialog_phone = false">+7 800 000 11 22</p>
        </div>
        </q-dialog>
    </q-header>
</template>
<script setup lang="ts">
import { ref } from 'vue';

var dialog = ref<boolean>(false)
var dialog_phone = ref<boolean>(false)
</script>