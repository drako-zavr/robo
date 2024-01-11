<template>
  <q-card class="team-card flex column justify-start no-box-shadow q-pa-lg">

    <q-img class="team-card__img" v-if="teammate?.photo" :src="teammate.photo"
      :height="`${$q.screen.lt.sm ? '306' : '500'}px`" :width="`${$q.screen.lt.sm ? '220' : '360'}px`" />
    <div>
      <p class="team-card__name text-secondary">{{ teammate?.name }} {{ teammate?.surname }}</p>
      <p class="team-card__position text-subtitle1">{{ teammate?.position }}</p>
      <a class="team-card__details text-accent cursor-pointer" @click="dialog = true">Подробнее</a>
    </div>

    <q-dialog v-model="dialog" ref="dialogRef">
      <q-card class="details-card flex column justify-start q-pa-md hide-scrollbar">
        <q-card-section class="details-card__content col q-pa-md">
          <div class="row">
            <q-btn flat no-caps v-close-popup class="details-card__close cursor-pointer gt-sm">Закрыть</q-btn>
            <img v-close-popup src="../assets/images/close_modal.svg" class="details-card__cross cursor-pointer lt-md">
            <q-img class="col details-card__photo" v-if="teammate?.photo" :src="teammate.photo"/>
            <div class="col">
              <p class="details-card__name text-secondary q-mb-sm">{{ teammate?.name }} {{ teammate?.surname }}</p>
              <p class="details-card__position q-mb-sm">{{ teammate?.position }}</p>
              <div class="row">
                <q-img class="details-card__social cursor-pointer q-mr-sm" src="../assets/images/Facebook.svg" alt="facebook"/>
                <q-img class="details-card__social cursor-pointer" src="../assets/images/Instagram.svg" alt="instagram"/>
              </div>
            </div>
          </div>
          <p class="details-card__info text-accent">Информация</p>
          <hr class="details-hr no-border q-mb-lg gt-xs">
          <p class="details-card__text" v-html="teammate?.info"></p>
        </q-card-section>
      </q-card>
    </q-dialog>

  </q-card>
</template>
<script setup lang="ts">
import { Teacher } from '../models/teacher';
import { PropType, ref } from 'vue';
import { useQuasar } from 'quasar'
defineProps({
  teammate: Object as PropType<Teacher>
});

const $q = useQuasar()
var dialog = ref<boolean>(false)


</script>