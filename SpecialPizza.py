from telegram.ext import *
import logging
import coon_dbpedia as dbpedia
import conn_pizza as SpecialPizza
import spacy_bot as txtSpacy
import telegram
import logging

img_pizza = "https://ibb.co/RCGy3jg"

# Set up the logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

def start_command(update, context):
    update.message.reply_text(
        'Hola, soy tu agente de SpecialPizza.\n\nA continuación te mostraré información de nuestras pizzas!')
    
    #update.message.reply_text(img_pizza)
    update.message.reply_text(
        "Escribe o pincha un comando para comenzar:\n"
        "\n/dbpedia     -> Accedemos a las pizzas de dbpedia"
        "\n/owl         -> Accedemos a nuestra propia ontología de SpecialPizzas"
        "\n/nlp         -> Probemos Procesamiento de Lenguaje Natural"
        )

########################################################################################### 

def types_command_dbpedia(update, context):
    qres = dbpedia.get_response_dbpedia_pizzasEs()
    
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        pais = result['pais1']['value']
        imagen_url = result['imagen']['value']
        comment = result['comment']['value']
        ingredientes = result['mainingredients']['value']
        update.message.reply_text('Nombre de la pizza : ' + name +
                                  '\n\nPaís de origen: ' + pais +
                                  '\n' + imagen_url + 
                                  '\n\nDescripción: ' + comment +
                                  '\n\nIngredientes: ' + ingredientes)
        
    update.message.reply_text(
        "Escribe o pincha un comando para seguir interactuando:\n"
        "\n/dbpedia     -> Accedemos a las pizzas de dbpedia"
        "\n/owl         -> Accedemos a nuestra propia ontología de SpecialPizzas"
        )

########################################################################################### 

def types_command_owl_typePizzas(update, context):
    update.message.reply_text("Escribe o pincha un tipo de pizza:")
    
    update.message.reply_text(
        "Escribe o pincha un comando para seguir interactuando :\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )
###########################################################################################      

def types_command_owl_tradicionalPizzas(update, context):
    update.message.reply_text("Nuestras pizzas tradicionales:")    
    qres = SpecialPizza.consultar_owl_TradicionalPizza()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /hawaiana /pepperoni /naturista")       
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )
    
def types_command_owl_PizzaHawaiana(update, context):
    update.message.reply_text("Ingredientes de Pizza Hawaiana")    
    qres = SpecialPizza.consultar_owl_pizzaHawaiana()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /hawaiana /pepperoni /naturista")       
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )

def types_command_owl_PizzaPepperoni(update, context):
    update.message.reply_text("Ingredientes de Pizza Pepperoni")    
    qres = SpecialPizza.consultar_owl_pizzaPepperoni()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /hawaiana /pepperoni /naturista")       
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )   
        
def types_command_owl_PizzaNaturista(update, context):
    update.message.reply_text("Ingredientes de Pizza Naturista")    
    qres = SpecialPizza.consultar_owl_pizzaNaturista()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)   
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /hawaiana /pepperoni /naturista")       
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )
        
###########################################################################################   
     
def types_command_owl_EventosPizzas(update, context):
    update.message.reply_text("Nuestras pizzas para eventos:")    
    qres = SpecialPizza.consultar_owl_EventoPizza()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /navidad /sanvalentin /halloween")  
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )    
        
def types_command_owl_PizzaNavidad(update, context):
    update.message.reply_text("Ingredientes de Pizza Navidad")    
    qres = SpecialPizza.consultar_owl_pizzaNavidad()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)  
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /navidad /sanvalentin /halloween")  
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )      
        
def types_command_owl_PizzaSanValentin(update, context):
    update.message.reply_text("Ingredientes de Pizza San Valentín")    
    qres = SpecialPizza.consultar_owl_pizzaSanValentin()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)   
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /navidad /sanvalentin /halloween")  
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )   
        
def types_command_owl_PizzaHalloween(update, context):
    update.message.reply_text("Ingredientes de Pizza Halloween")    
    qres = SpecialPizza.consultar_owl_pizzaHalloween()
    for i in range(len(qres['results']['bindings'])):
        result = qres['results']['bindings'][i]
        name = result['name']['value']
        update.message.reply_text(name)  
    update.message.reply_text("Mira los ingredientes de alguna pizza. \nPincha en una: /navidad /sanvalentin /halloween")  
    update.message.reply_text(
        "O escribe o pincha un comando para seguir interactuando con otro tipo de pizza:\n"
        "\n/pizzasEventos           -> Accedemos a nuestras pizzas para eventos"
        "\n/pizzasTradicionales     -> Accedemos a nuestras pizzas tradicionales"
        )   
        
###########################################################################################   

def nlp_dbpedia(update, context):
    update.message.reply_text("Ingresa un texto")
    bot = context.bot
    updateMsg = getattr(update, 'message', None)
    messageId = updateMsg.message_id #obtengo el id del mensaje
    chatId = update.message.chat_id
    #txt = update.effective_user['texto']
    mytxt = update.message.text #obtener el texto que envio el usuario
    print(mytxt)
    #update.message.reply_text(mytxt)
    
    doc = txtSpacy.spacy_info(mytxt)
    for w in doc:
        a = w.text, w.pos_
        update.message.reply_text(a)
        print(a)
        #print(w.text, w.pos_)

if __name__ == '__main__':
    updater = Updater(token="1852245381:AAGVgxLhVpduGLi3AKViWw9qqbnUdwBqw6Ia97", use_context=True)

    dp = updater.dispatcher
    # -------------------------------------------------------
    dp.add_handler(CommandHandler('start', start_command))

    dp.add_handler(CommandHandler('dbpedia', types_command_dbpedia))
    
    dp.add_handler(CommandHandler('owl', types_command_owl_typePizzas))
    
    dp.add_handler(CommandHandler('nlp', nlp_dbpedia))
    
    dp.add_handler(CommandHandler('pizzasTradicionales', types_command_owl_tradicionalPizzas))
    
    dp.add_handler(CommandHandler('pizzasEventos', types_command_owl_EventosPizzas))
    
    dp.add_handler(CommandHandler('navidad', types_command_owl_PizzaNavidad))
    
    dp.add_handler(CommandHandler('halloween', types_command_owl_PizzaHalloween))
    
    dp.add_handler(CommandHandler('sanvalentin', types_command_owl_PizzaSanValentin))
    
    dp.add_handler(CommandHandler('hawaiana', types_command_owl_PizzaHawaiana)) 
    
    dp.add_handler(CommandHandler('pepperoni', types_command_owl_PizzaPepperoni))
    
    dp.add_handler(CommandHandler('naturista', types_command_owl_PizzaNaturista))
    
    dp.add_handler(MessageHandler(Filters.text, nlp_dbpedia))
    #--------------------------------------------------------
    dp.add_error_handler(error)
    updater.start_polling(1.0)
    updater.idle()
