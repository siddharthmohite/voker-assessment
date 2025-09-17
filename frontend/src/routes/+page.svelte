<script lang="ts">
import { onMount } from 'svelte';

let ordersDict:  Record<string, { burgers: number; fries: number; drinks: number }> = {};
let orderTotals: Record<string, number> = {};
let query = ""

async function sendChat(query: string){

    try{
        const res  = await fetch('http://127.0.0.1:8000/send_chat', {
        method : "POST",
        headers: {
            "Content-Type":"application/json",
    },
    body : JSON.stringify({input: query})
    
});
const data = await res.json();
console.log("data", data);

if(res.ok){
    fetch_total_orders();
    fetch_order_history();
}
    }
    catch(err){
        console.log(err);
    }
};

async function fetch_order_history(){
       try{
        const res = await fetch('http://127.0.0.1:8000/orders')
        const ordersArray = await res.json();
        
        ordersDict = {};
        for (const order of ordersArray)
    {
        ordersDict[order.order_number] ={
            burgers : order.burgers ,
            fries : order.fries,
            drinks: order.drinks
        };
    }
        
    }
    catch(err){
        console.log(err)
    }
}

async function fetch_total_orders(){
        try{
            const res  = await fetch('http://127.0.0.1:8000/orders/totals')
            orderTotals = await res.json();

    }
    catch(err){
        console.log("Error while fetching order totals ", err);
    }

}
onMount(async () =>{

    fetch_order_history();
    fetch_total_orders();
});

</script>

<main>

<div class="container">
    <h1 class="title">Drive Thru Ordering System</h1>
    <div class ="t-holder">
        <div class="total">
            <h1 class="text">Total number of Burgers: {orderTotals.burgers}</h1>
        </div>
        <div class="total">
            <h1 class="text">Total number of Fries: {orderTotals.fries}</h1>

        </div>
        <div class="total">
            <h1 class="text">Total number of Drinks: {orderTotals.drinks}</h1>

        </div>
    </div>
    <div class="t-holder">
        <input class="input" bind:value={query} placeholder="Type your message here" />
        <div class="run">
            <button on:click={() => sendChat(query)}>Run</button>
        </div>
    </div>
    <div class="o-holder">
        {#each Object.entries(ordersDict) as [num , o]}
        <ul>
            <li class="list-item">
            <p class="list-item-text">Order#{num} : {o.burgers} burgers, {o.fries} Fries, {o.drinks} Drinks</p>
            </li>
        </ul>
        {/each}
    </div>
</div>
       



</main>

<style>
    .container{
        display: flex;
        flex-direction:column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        gap:3rem;
    }
    .title{
        color: Black;
        font-size: 3rem;
    }
    .t-holder{
        display: flex;
        flex-direction: row;
        gap: 1rem;
    }
    .o-holder{
         display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    .total{
        display: flex;
        padding: 2rem;
        background-color: brown;
    }
    .run{
        display:flex;
        background: red;
        border-radius: 50%;
        color:white;
        padding: 0.5rem;
        margin-left: 3rem;
    }
    .list-item{
        display:flex;
        background:green;
        padding: 0.5rem; 
    }
    .list-item-text{
        color:white;
    }
    .text{
        color: white;
    }
    .input{
        display:flex;
    }
</style>