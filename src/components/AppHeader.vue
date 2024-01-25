<template>
    <SectionBlock bgClass="bg-secondary">
        <div class="main-header text-primary bg-secondary relative-position"> 
            <img src="../assets/images/girl.png" class="main-header__img q-mx-auto absolute-bottom-right">
            <div class=" q-container row">
                <p class="main-header__title q-mb-md q-px-md text-h2 text-weight-medium">ROBO SCHOOL</p>
                <p class="main-header__text q-mb-xl col-12 q-px-md text-h6 text-weight-regular">
                    Курсы повышения квалификации по робототехнике <br>для педагогов начальной школы
                </p>
                <q-btn no-caps href="#price" class="main-header__btn text-weight-regular bg-accent q-ml-md q-px-xl q-py-lg text-body1">Записаться на курс</q-btn>
        </div></div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>