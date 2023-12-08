<template>
    <!-- <div class="details-card-wrapper"> -->
    <q-dialog ref="dialogRef">
        <q-card class="details-card flex column justify-start q-pa-md  ">

            <q-card-section class="details-card__content col">
                <div class="row">
                    <a class="details-card__close">Закрыть</a>
                    <img class="col details-card__photo">
                    <div class="col">
                        <p class="details-card__title">{{ teammate?.name }}</p>
                        <p class="details-card__position">{{ teammate?.position }}</p>
                        <div class="row">
                            <img src="" alt="">
                            <img src="" alt="">
                        </div>
                    </div>
                </div>
                <p class="details-card__info">Информация</p>
                <p class="details-card__text">{{ teammate?.position }}</p>
            </q-card-section>

        </q-card>
    </q-dialog>
</template>
<script setup lang="ts">
import { Teacher } from '../types/index';
import { PropType } from 'vue';
defineProps({
    teammate: Object as PropType<Teacher>
});
console.log('a')

</script>