
{
	'name': 'Modulo Especial Para Rodbal',
	
	'version': '12.0',
       
	'summary': 'Rodbal - Intresoc',
	'description': """
Plantillas de Reportes Colombia:
======================
	* Este módulo realiza unos ajustes a distintas vistas para que sea mas facil la operación de los administradores.
	
	""",
	'depends': [
		
		'account','purchase',
	],
	'data': [
		
		'views/purchase_view_custom.xml'	
		
	],
	'installable': True,
	'application': True,
}
