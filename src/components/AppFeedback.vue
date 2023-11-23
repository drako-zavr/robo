<template>
    <SectionBlock
    bgClass="bg-accent"
    >
        <div class="q-container ">
      <div class="row">
        <div class="col-6 q-pb-md text-white">
          <p class="feedback__title">Запишитесь на курс со скидкой 10%</p>
          <p class="feedback__text"> Акция действительна до 10 марта 2022 года</p>
        </div>
        <div class= 'col-6' >
          <FeedbackForm />
        </div>
        
        
      </div>
      
    </div>
    <div class="row w-100">
            <img class="col percent"
    height="120"
    src="~images/percent.svg"
  />
  <img class="col percent"
    height="120"
    src="~images/percent.svg"
  />
  
        </div>
    </SectionBlock>

</template>
<script setup lang="ts">
import FeedbackForm from './FeedbackForm.vue';
import SectionBlock from './SectionBlock.vue';
</script>