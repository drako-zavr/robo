<template>
  <q-card class="team-card flex column justify-start no-box-shadow q-pa-lg">
    <q-img class="team-card__img" v-if="teammate?.photo" :src="teammate.photo"/> 
    <div>
      <p class="team-card__name text-secondary text-h5 text-weight-medium">{{ teammate?.name }} {{ teammate?.surname }}</p>
      <p class="team-card__position text-subtitle1 q-mb-lg text-info">{{ teammate?.position }}</p>
      <a class="team-card__details text-accent cursor-pointer text-subtitle1" @click="dialog = true">Подробнее</a>
    </div>

    <q-dialog v-model="dialog" ref="dialogRef">
      <q-card class="details-card column q-pa-md hide-scrollbar">
        <q-card-section class="details-card__content col q-pa-md q-mb-xl">
          <img v-close-popup src="../assets/images/close_modal.svg" class="cursor-pointer lt-md absolute-top-right q-mt-sm q-mr-sm">
          <div class="row">
            <q-btn flat no-caps v-close-popup class="details-card__close cursor-pointer gt-sm absolute-top-right q-mt-sm q-mr-lg text-info">Закрыть</q-btn>
            <q-img class="col details-card__photo q-mr-xl q-mb-xl" v-if="teammate?.photo" :src="teammate.photo"/>
            <div class="col">
              <p class="details-card__name text-secondary q-mb-sm text-h5 text-weight-medium">{{ teammate?.name }} {{ teammate?.surname }}</p>
              <p class="details-card__position q-mb-sm text-subtitle1 text-info">{{ teammate?.position }}</p>
              <div class="row">
                <q-img class="details-card__social cursor-pointer q-mr-sm" src="../assets/images/Facebook.svg" alt="facebook"/>
                <q-img class="details-card__social cursor-pointer" src="../assets/images/Instagram.svg" alt="instagram"/>
              </div>
            </div>
          </div>
          <p class="text-accent q-mb-md text-weight-regular text-h6">Информация</p>
          <q-separator class=" q-mb-lg gt-xs"> ></q-separator>
          <p class="details-card__text q-mb-xl q-mr-xl text-h6 text-weight-regular" v-html="teammate?.info"></p>
        </q-card-section>
      </q-card>
    </q-dialog>

  </q-card>
</template>
<script setup lang="ts">
import { Teacher } from '../models/teacher';
import { PropType, ref } from 'vue';

defineProps({
  teammate: Object as PropType<Teacher>
});

var dialog = ref<boolean>(false)

</script>