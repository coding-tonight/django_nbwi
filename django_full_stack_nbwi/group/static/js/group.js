const DeleteFunction = (id) => {
   axios.delete('group/delete/' + id)
   .then(response => console.log(response.data))
   .catch(error => console.log(error))
}