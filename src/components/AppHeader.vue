<template>
    <SectionBlock bgClass="bg-secondary">
        <div class="main-header text-primary bg-secondary">
            <img src="../assets/images/girl.png" class="main-header__img ">
            <div class="q-container">
                <div class="row">
                    <div class="main-header__title col-12">
                        <p>ROBO SCHOOL</p>
                    </div>
                    <div class="main-header__text col-12 q-mb-xl">
                        <p>Курсы повышения квалификации по робототехнике <br>для педагогов начальной школы</p>
                    </div>
                    <q-btn no-caps href="#price" class="main-header__btn text-weight-regular bg-accent">Записаться на курс</q-btn>
                </div> 
            </div>
            
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>