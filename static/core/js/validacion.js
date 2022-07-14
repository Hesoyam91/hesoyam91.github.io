var nombre = document.getElementById('Nombre');
var rut = document.getElementById('rut');
var email = document.getElementById('email');
var password = document.getElementById('password');
var region = document.getElementById('region');
var comuna = document.getElementById('comuna');
var mascota = document.getElementById('mascota');
var animal = document.getElementById('animal');
var numero = document.getElementById('numero');
var error= document.getElementById('error');
error.style.color = 'red'

var form = document.getElementById('formulario');
    form.addEventListener('submit', function(evt){
        evt.preventDefault();
        var mensajesError =  [];        

                if(nombre.value === null || nombre.value === ''){
                     mensajesError.push('Ingresa tu nombre')
        
                } else if(rut.value === null || rut.value === ''){
                     mensajesError.push('Ingresa tu rut')
        
                } else if(email.value === null || email.value === ''){
                     mensajesError.push('Ingresa tu email')
        
                } else if(password.value === null || password.value === ''){
                     mensajesError.push('Ingresa tu contraseña')
        
                } else if(region.value === null || region.value === ''){
                     mensajesError.push('Ingresa tu region')
        
                } else if(comuna.value === null || comuna.value === ''){
                     mensajesError.push('Ingresa tu comuna')
        
                } else if(mascota.value === null || mascota.value === ''){
                     mensajesError.push('Ingresa el nombre de tu mascota')
        
                } else if(animal.value === null || animal.value === ''){
                     mensajesError.push('Ingresa el tipo de animal')
        
                } else if(numero.value === null || numero.value === ''){
                     mensajesError.push('Ingresa tu número')
       
               } else{                
                     mensajesError.push('¡Lo contactaremos muy pronto!')
            }
        

        












                

             
        
                error.innerHTML = mensajesError.join(', ');
        
             
        
    });
    