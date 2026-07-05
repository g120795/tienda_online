### arquitectura
    ##concepto:conjunto de tablas referenciadas por llaves foraneas persistente.
    
    ##flujo interno.

        user

            ↓

        product

            ↓

        order

            ↓
        
        orderitem


### diseño
    ## el carrito es un estado de order
    #ventaja:simple
    #desventaja:se necesitara modificar o crear un modelo en el futuro para ser escalable.
    #en retrospectiva: templates en la raiz del proyecto, para centralizar
    