<template>
  <q-card class="team-card flex column justify-start q-pa-md col">

    <q-img class="team-card__img" v-if="teammate?.photo" :src="teammate.photo"
      :height="`${$q.screen.lt.sm ? '306' : '500'}px`" :width="`${$q.screen.lt.sm ? '220' : '360'}px`" />
    <div>
      <p class="team-card__name">{{ teammate?.name }}</p>
      <p class="team-card__position text-subtitle1">{{ teammate?.position }}</p>
      <a class="team-card__details" @click="dialog = true">Подробнее</a>
    </div>
  <!-- <DetailsCard v-if="showMore" :teammate="teammate" /> -->

  <q-dialog v-model="dialog" ref="dialogRef">
        <q-card class="details-card flex column justify-start q-pa-md  ">

            <q-card-section class="details-card__content col">
                <div class="row">
                    <a class="details-card__btn ">Закрыть</a>
                    <img class="col details-card__photo" v-if="teammate?.photo" :src="teammate.photo">
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
                <p class="details-card__text">{{ teammate?.info }}</p>
            </q-card-section>

        </q-card>
        
    </q-dialog>
  


  
  </q-card>

</template>
<script setup lang="ts">
// import DetailsCard from 'src/components/DetailsCard.vue';
import { Teacher } from '../types/index';
import { PropType, ref } from 'vue';
import { useQuasar } from 'quasar'
defineProps({
  teammate: Object as PropType<Teacher>
});

const $q = useQuasar()
var dialog = ref(false)
// var teacherDetails




</script>