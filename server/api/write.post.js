export default defineEventHandler(async (event) => {
    const error = '';
    const body = await readBody(event)
    const jsonBody = JSON.stringify(body)
  
   await useStorage().setItem(`assets/server/formres.json`, jsonBody)  
 
    return {
        body: "sucess"
    }
})