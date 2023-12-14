<template>
    <SectionBlock
    bgClass="feedback-section"
    >
        <div class="feedback q-container ">
      <div class="feedback__row row">
        <div class="feedback__desc col-6-md col-6-lg col-12-sm  text-white">
          <p class="feedback__title">Запишитесь на курс <br>со скидкой 10%</p>
          <p class="feedback__text"> Акция действительна до 10 марта 2022 года</p>
        </div>
        
          <FeedbackForm />
        
        
        
      </div>
      
    </div>
    <div class="row w-100">
            <!-- <img class="col percent"
    height="120"
    src="~images/percent2.png"
  /> -->
  <!-- <img class="col percent"
    height="120"
    src="~images/percent1.svg"
  /> -->
  
        </div>
    </SectionBlock>

</template>
<script setup lang="ts">
import FeedbackForm from './FeedbackForm.vue';
import SectionBlock from './SectionBlock.vue';
</script>