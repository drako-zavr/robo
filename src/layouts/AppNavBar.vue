<template>
    <q-header reveal class="navbar bg-secondary q-px-xl">
        <q-toolbar class=" bg-transparent q-pa-md">
            <q-toolbar-title class="navbar__title text-left text-weight-bold "> ROBO.SCHOOL </q-toolbar-title>
            <q-btn flat no-caps class="navbar__link gt-sm q-mr-xl" href="#school"> О школе </q-btn>
            <q-btn flat no-caps class="navbar__link gt-sm q-mr-xl" href="#teachers"> Тренеры </q-btn>
            <q-btn flat no-caps class="navbar__link gt-sm" href="#price"> Стоимость </q-btn>
            <q-toolbar-title class="navbar__phone text-right gt-sm"> +7 800 000 11 22 </q-toolbar-title>

            <q-img src="../assets/images/phone.png" class="navbar__menu-btn lt-md" @click="dialog_phone = true" />
            <q-img src="../assets/images/menu.png" class="navbar__menu-btn q-ml-sm lt-md" @click="dialog = true" />
        </q-toolbar>

        <q-dialog  v-model="dialog" class="modal bg-secondary text-center text-primary">
            <img src="../assets/images/close.png" class="modal__btn q-pa-md absolute-top-right" @click="dialog = false">
            <div class="col">
                <q-btn flat no-caps class="modal__link col-12 w-100 q-mb-lg" href="#school" @click="dialog = false">О школе</q-btn>
                <q-btn flat no-caps class="modal__link col-12 w-100 q-mb-lg" href="#teachers"
                    @click="dialog = false">Тренеры</q-btn>
                <q-btn flat no-caps class="modal__link col-12 w-100 q-mb-lg" href="#price" @click="dialog = false">Стоимость</q-btn>
            </div>
        </q-dialog>
        <q-dialog v-model="dialog_phone" class="modal bg-secondary text-primary text-center">
            <img src="../assets/images/close.png" class="modal__btn q-pa-md absolute-top-right" @click="dialog_phone = false">
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