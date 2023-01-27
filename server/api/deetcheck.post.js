export default defineEventHandler(async (event) => {
    const error = '';
    const body = await readBody(event)
    if(body.username === 'Admin' && body.password === 'Password123!'){
        return {
            data: 'sucess'
        }
    }else {
        return  {
            error: "not valid"
        }
    }

})