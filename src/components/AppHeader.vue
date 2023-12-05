<template>
    <SectionBlock bgClass="bg-secondary">
        <div class="main-header ">
            <img src="../assets/images/girl.png" alt="" class="main-header__img" :class="$q.screen.gt.sm ? '' : 'main-header__img_sm'">
            <div class="q-container">
                <div class="row">
                    <!-- <div class="col-12"></div> -->
                    <div class="main-header__title col-12" :class="$q.screen.gt.sm ? '' : 'main-header__title_sm text-center'">
                        <p>ROBO SCHOOL</p>
                    </div>
                    <div class="main-header__text col-12" :class="$q.screen.gt.sm ? '' : 'main-header__text_sm text-center'">
                        Курсы повышения квалификации по робототехнике <br>для педагогов начальной школы
                    </div>
                    <a href="#" class="main-header__btn" :class="$q.screen.gt.sm ? '' : 'main-header__btn_sm'">Записаться на курс</a>
                </div>
            </div>
            
        </div>
    </SectionBlock>
</template>
<script setup lang="ts">
import SectionBlock from './SectionBlock.vue';
</script>