<template>
    <SectionBlock bgClass="bg-secondary">
        <div class="main-header text-primary bg-secondary relative-position q-container row">
            <img src="../assets/images/girl.png" class="main-header__img q-mx-auto absolute-bottom-right">
                <p class="main-header__title q-mb-md q-px-md">ROBO SCHOOL</p>
                <p class="main-header__text q-mb-xl col-12 q-px-md">
                    Курсы повышения квалификации по робототехнике <br>для педагогов начальной школы
                </p>
                <q-btn no-caps href="#price" class="main-header__btn text-weight-regular bg-accent q-ml-md q-px-xl q-py-lg">Записаться на курс</q-btn>
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>