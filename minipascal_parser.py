import ply.yacc as yacc
from minipascal_lexer import tokens
import sys

VERBOSE = 1

#------------------------------------ PROGRAMS AND BLOCKS ----------------------------------------------
def p_program(p):
	'program : program_heading block DOT'
	pass

def p_program_heading(p):
	'''program_heading : PROGRAM identifier SEMICOLON
					   | PROGRAM identifier LPAREN identifier_list RPAREN SEMICOLON'''
	pass

def p_block(p):
	'block : declaration_part statement_part'
	pass

def p_declaration_part(p):
	'''declaration_part : label_declaration_part procedure_and_function_declaration_part
						|  label_declaration_part constant_definition_part procedure_and_function_declaration_part
						|  label_declaration_part type_definition_part procedure_and_function_declaration_part
						|  label_declaration_part variable_declaration_part procedure_and_function_declaration_part
						|  label_declaration_part constant_definition_part type_definition_part procedure_and_function_declaration_part
						|  label_declaration_part constant_definition_part type_definition_part variable_declaration_part procedure_and_function_declaration_part
						|  label_declaration_part constant_definition_part variable_declaration_part procedure_and_function_declaration_part					
						|  label_declaration_part type_definition_part variable_declaration_part procedure_and_function_declaration_part
						|	constant_definition_part procedure_and_function_declaration_part
						|	constant_definition_part type_definition_part procedure_and_function_declaration_part
						|	constant_definition_part variable_declaration_part procedure_and_function_declaration_part
						|	constant_definition_part type_definition_part variable_declaration_part procedure_and_function_declaration_part
						|	type_definition_part procedure_and_function_declaration_part
						|	type_definition_part variable_declaration_part procedure_and_function_declaration_part
						|	procedure_and_function_declaration_part
	'''
	pass

def p_label_declaration_part(p):
	'label_declaration_part : LABEL label_list SEMICOLON'
	pass

def p_label_list(p):
	'''label_list : label
				| label_list COMMA label'''
	pass

def p_constant_definition_part(p):
	'constant_definition_part : CONST constant_definition_list SEMICOLON'
	pass

def p_constant_definition_list(p):
	'''constant_definition_list : constant_definition 
							| constant_definition_list SEMICOLON constant_definition'''
	pass

def p_constant_definition(p):
	'constant_definition : identifier EQUAL constant'
	pass

def p_type_definition_part(p):
	'type_definition_part : TYPE type_definition_list SEMICOLON'
	pass

def p_type_definition_list(p):
	'''type_definition_list : type_definition
							| type_definition_list SEMICOLON type_definition'''
	pass

def p_type_definition(p):
	'type_definition : identifier EQUAL type'
	pass

def p_variable_declaration_part(p):
	'variable_declaration_part : VAR variable_declaration_list SEMICOLON'
	pass

def p_variable_declaration_list(p):
	'''variable_declaration_list : variable_declaration
								| variable_declaration_list SEMICOLON variable_declaration'''
	pass

def p_variable_declaration(p):
	'variable_declaration : identifier_list COLON type'
	pass

def p_procedure_and_function_declaration_part(p):
	'''procedure_and_function_declaration_part : procedure_declaration SEMICOLON
												| function_declaration SEMICOLON '''
	pass

def p_procedure_declaration(p):
	'''procedure_declaration : procedure_heading SEMICOLON procedure_body
							| procedure_heading SEMICOLON directive
							| procedure_identification SEMICOLON procedure_body
	'''
	pass

def p_procedure_body(p):
	'procedure_body : block'
	pass

def p_function_declaration(p):
	'''function_declaration : function_heading SEMICOLON function_body
							| function_heading SEMICOLON directive
							| function_identification SEMICOLON function_body
	'''
	pass

def p_function_body(p):
	'function_body : block'
	pass

def p_directive(p):
	'directive : FORWARD'
	pass

def p_statement_part(p):
	'statement_part : BEGIN statement_sequence END'
	pass

#----------------------------------- PROCEDURE AND FUNCTION DEFINITIONS ------------------------------------


def p_procedure_heading(p):
	'''procedure_heading : PROCEDURE identifier
						| PROCEDURE identifier formal_parameter_list'''
	pass

def p_function_heading(p):
	'''function_heading : FUNCTION identifier COLON result_type
						| FUNCTION identifier formal_parameter_list COLON result_type'''
	pass

def p_result_type(p):
	'result_type : type_identifier'
	pass

def p_procedure_identification(p):
	'procedure_identification : PROCEDURE procedure_identifier'
	pass

def p_function_identification(p):
	'function_identification : FUNCTION function_identifier'
	pass

def p_formal_parameter_list(p):
	'formal_parameter_list : LPAREN formal_parameter_section_list RPAREN'
	pass

def p_formal_parameter_section_list (p):
	'''formal_parameter_section_list : formal_parameter_section
									| formal_parameter_section_list SEMICOLON formal_parameter_section'''
	pass

def p_formal_parameter_section(p):
	'''formal_parameter_section : value_parameter_section
								| variable_parameter_section
								| procedure_parameter_section
								| function_parameter_section'''
	pass

def p_value_parameter_section(p):
	'value_parameter_section : identifier_list COLON parameter_type'
	pass

def p_variable_parameter_section(p):
	'variable_parameter_section : VAR identifier_list COLON parameter_type'
	pass

def p_procedure_parameter_section(p):
	'procedure_parameter_section : procedure_heading'
	pass

def p_function_parameter_section(p):
	'function_parameter_section : function_heading'
	pass

def p_parameter_type(p):
	'''parameter_type : type_identifier
					| conformant_array_schema'''
	pass

def p_conformant_array_schema(p):
	'''conformant_array_schema : packed_conformant_array_schema
							| unpacked_conformant_array_schema'''
	pass

def p_packed_conformant_array_schema(p):
	'packed_conformant_array_schema : PACKED ARRAY LBRACKET bound_specification RBRACKET OF type_identifier'
	pass

def p_unpacked_conformant_array_schema(p):
	'''unpacked_conformant_array_schema : ARRAY LBRACKET bound_specification_list RBRACKET OF type_identifier
										| ARRAY LBRACKET bound_specification_list RBRACKET OF conformant_array_schema'''
	pass

def p_bound_specification_list(p):
	'''bound_specification_list : bound_specification
								| bound_specification_list SEMICOLON bound_specification'''
	pass

def p_bound_specification(p):
	'bound_specification : identifier RANGE_OPERATOR identifier SEMICOLON ordinal_type_identifier'
	pass

def p_ordinal_type_identifier(p):
	'ordinal_type_identifier : type_identifier'
	pass

#---------------------------------------------- STATEMENTS -------------------------------------------
def p_statement_sequence(p):
	'statement_sequence : statement'
	pass

def p_statement_sequence_1(p):
	'statement_sequence : statement SEMICOLON statement'
	pass

def p_statement(p):
	'''
	statement : label COLON simple_statement
			| label COLON structured_statement
			| simple_statement
			| structured_statement
	'''
	pass

def p_simple_statement(p):
	'''simple_statement : assignment_statement
						| procedure_statement
						| goto_statement
						'''
	pass

def p_assignment_statement(p):
	'''assignment_statement : variable ASSIGN expression
							| function_identifier ASSIGN expression'''
	pass

def p_procedure_statement(p):
	'''procedure_statement : procedure_identifier 
						| procedure_identifier actual_parameter_list'''
	pass

def p_goto_statement(p):
	'goto_statement : GOTO label'
	pass

def p_structured_statement(p):
	'''structured_statement : compound_statement 
							| repetitive_statement 
							| conditional_statement 
							| with_statement'''
	pass

def p_compound_statement(p):
	'compound_statement : BEGIN statement_sequence END'
	pass

def p_repetitive_statement(p):
	'''repetitive_statement : while_statement 
						| repeat_statement 
						| for_statement'''
	pass

def p_while_statement(p):
	'while_statement : WHILE expression DO statement'
	pass

def p_repeat_statement(p):
	'repeat_statement : REPEAT statement_sequence UNTIL expression'
	pass

def p_for_statement(p):
	'''for_statement : FOR variable_identifier ASSIGN initial_expression TO final_expression DO statement
					| FOR variable_identifier ASSIGN initial_expression DOWNTO final_expression DO statement'''
	pass

def p_initial_expression(p):
	'initial_expression : expression'
	pass

def p_final_expression(p):
	'final_expression : expression'
	pass

def p_conditional_statement(p):
	'''conditional_statement : if_statement
							| case_statement'''
	pass

def p_if_statement(p): 
	'''if_statement : IF expression THEN statement
					| IF expression THEN statement ELSE statement'''
	pass

def p_case_statement(p):
	'''case_statement : CASE expression OF case_limb_list END
					| CASE expression OF case_limb_list SEMICOLON END'''
	pass

def p_case_limb_list(p): 
	'''case_limb_list : case_limb
					| case_limb_list SEMICOLON case_limb'''
	pass

def p_case_limb(p):
	'case_limb : case_label_list COLON statement'
	pass

def p_case_label_list(p):
	'''case_label_list : constant
					| case_label_list COMMA constant'''
	pass

def p_with_statement(p):
	'with_statement : WITH record_variable_list DO statement'
	pass

def p_record_variable_list(p):
	'''record_variable_list : record_variable
							| record_variable_list COMMA record_variable'''
	pass

def p_actual_parameter_list(p):
	'actual_parameter_list : LPAREN actual_parameter_list2 RPAREN'
	pass

def p_actual_parameter_list2(p):
	'''actual_parameter_list2 : actual_parameter
							| actual_parameter_list2 COMMA actual_parameter'''
	pass

def p_actual_parameter(p):
	'''actual_parameter : actual_value
						| actual_variable
						| actual_procedure
						| actual_function'''
	pass

def p_actual_value(p):
	'actual_value : expression'
	pass

def p_actual_procedure(p):
	'actual_procedure : procedure_identifier'
	pass 

def p_actual_function(p):
	'actual_function : function_identifier'
	pass

#---------------------------------------------- EXPRESSIONS -------------------------------------------
def p_expression(p):
	'''expression : simple_expression
				| simple_expression relational_operator simple_expression'''
	pass

def p_simple_expression(p):
	'''simple_expression : sign term_list
						| term_list '''
	pass

def p_term_list(p):
	'''term_list : term
				| term_list addition_operator term'''
	pass

def p_term(p):
	'''term : factor
			| term multiplication_operator factor'''
	pass

def p_factor(p):
	'''factor : variable
			| number
			| string
			| set
			| NIL
			| constant_identifier 
			| bound_identifier 
			| function_designator 
			| LPAREN expression RPAREN 
			| NOT factor'''
	pass

def p_relational_operator(p):
	'''relational_operator : EQUAL
			| NOTEQUAL
			| LESS 
			| LESSEQUAL
			| GREATER
			| GREATEREQUAL
			| IN '''
	pass

def p_addition_operator(p):
	'''addition_operator : PLUS
			| MINUS
			| OR '''
	pass

def p_multiplication_operator(p):
	'''multiplication_operator : TIMES
			| DIVIDE
			| DIV
			| MOD
			| AND'''
	pass

def p_variable(p):
	'''variable : entire_variable 
			| component_variable 
			| referenced_variable'''
	pass

def p_entire_variable(p):
	'''entire_variable : variable_identifier 
			| field_identifier '''
	pass

def p_component_variable(p):
	'''component_variable : indexed_variable 
						| field_designator 
						| file_buffer '''
	pass

def p_indexed_variable(p):
	'indexed_variable : array_variable LBRACKET expression_list RBRACKET'
	pass

def p_field_designator(p):
	'field_designator : record_variable DOT field_identifier'
	pass

def p_set(p):
	'set : LBRACKET element_list RBRACKET'
	pass

def p_element_list(p):
	'''element_list : 
				| expression_list'''
	pass

def p_function_designator(p):
	'''function_designator :  function_identifier 
						| function_identifier actual_parameter_list'''
	pass

def p_file_buffer(p):
	'file_buffer : file_variable UPARROW'
	pass


#------------------------ TYPES ---------------------------------
def p_type(p):
	'''type : simple_type 
			| structured_type 
			| pointer_type 
			| type_identifier '''
	pass

def p_simple_type(p):
	'''simple_type : subrange_type 
				| enumerated_type'''
	pass

def p_enumerated_type(p):
	'enumerated_type : LPAREN identifier_list RPAREN'
	pass

def p_subrange_type(p): #MIRAR BIEN QUE ES ".."
	'subrange_type : lower_bound RANGE_OPERATOR upper_bound'
	pass

def p_lower_bound(p):
	'lower_bound : constant'
	pass

def p_upper_bound(p):
	'upper_bound : constant'
	pass

def p_structured_type(p):
	'''structured_type : PACKED unpacked_structured_type
					| unpacked_structured_type'''
	pass

def p_unpacked_structured_type(p):
	'''unpacked_structured_type : array_type 
							| record_type 
							| set_type 
							| file_type'''
	pass

def p_array_type(p):
	'array_type : ARRAY LBRACKET index_type_list RBRACKET OF element_type'
	pass

def p_index_type_list(p):
	'''index_type_list : index_type
					| index_type_list COMMA index_type '''
	pass

def p_index_type(p):
	'index_type : simple_type '
	pass

def p_element_type(p):
	'element_type : type'
	pass

def p_record_type (p):
	'record_type : RECORD field_list END'
	pass

def p_set_type (p):
	'set_type : SET OF base_type'
	pass

def p_base_type (p):
	'base_type : type'
	pass

def p_file_type (p):
	'file_type : FILE OF file_component_type'
	pass

def p_file_component_type(p):
	'file_component_type : type'
	pass

def p_pointer_type(p):
	'pointer_type : UPARROW type_identifier'
	pass


#------------------------------------ RECORD FIELDS ------------------------
def p_field_list(p):
	'''field_list : 
				| fixed_part
				| fixed_part SEMICOLON variant_part
				| fixed_part SEMICOLON variant_part SEMICOLON
				| variant_part
				| variant_part SEMICOLON'''
	pass

def p_fixed_part(p):
	'''fixed_part : record_section
				| fixed_part SEMICOLON record_section'''
	pass

def p_record_section(p):
	'record_section : identifier_list COLON type'
	pass

def p_variant_part(p):
	'variant_part : CASE tag_field type_identifier OF variant_list'
	pass

def p_variant_list(p):
	'''variant_list : variant
					| variant_list SEMICOLON variant'''
	pass

def p_tag_field(p):
	'''tag_field :   
				| identifier COLON'''
	pass

def p_variant(p):
	'variant : case_label_list SEMICOLON LPAREN field_list RPAREN'
	pass

#-------------------------------------------- INPUT / OUTPUT ---------------------------------------------
def p_output_list(p):
	'''output_list : output_value 
				| output_list COMMA output_value'''
	pass

def p_output_value(p):
	'''output_value : expression
				| expression SEMICOLON field_width
				| expression SEMICOLON field_width COLON fraction_length'''
	pass

def p_field_width(p):
	'field_width : expression'
	pass

def p_fraction_length(p):
	'fraction_length : expression'
	pass

#--------------------------------------- VARIABLE AND IDENTIFIER CATEGORIES -------------------------------
def p_identifier(p):
	'identifier : ID'
	pass

def p_file_variable(p):
	'file_variable : variable'
	pass

def p_freferenced_variable(p):
	'referenced_variable : pointer_variable UPARROW'
	pass

def p_record_variable(p):
	'record_variable : variable'
	pass

def p_pointer_variable(p):
	'pointer_variable : variable'
	pass

def p_actual_variable(p):
	'actual_variable : variable'
	pass

def p_array_variable(p):
	'array_variable : variable'
	pass

def p_field_identifier(p):
	'field_identifier : identifier'
	pass

def p_constant_identifier(p):
	'constant_identifier : identifier'
	pass

def p_variable_identifier(p):
	'variable_identifier : identifier'
	pass

def p_type_identifier(p):
	'type_identifier : identifier'
	pass

def p_procedure_identifier(p):
	'procedure_identifier : identifier'
	pass

def p_function_identifier(p):
	'function_identifier : identifier'
	pass

def p_bound_identifier(p):
	'bound_identifier : identifier'
	pass

#--------------------------------------- LOW LEVEL DEFINITIONS ------------------------------------

def p_variable_list(p):
	'''variable_list : variable
					| variable_list COMMA variable'''
	pass

def p_identifier_list(p):
	'''identifier_list : identifier
					| identifier_list COMMA identifier'''
	pass

def p_expression_list(p):
	'''expression_list : expression
					| expression_list COMMA expression'''
	pass

def p_number(p):
	'''number : integer_number
			  | real_number'''
	pass

def p_integer_number(p):
	'integer_number : digit_sequence'
	pass

def p_real_number(p):
	'''real_number : digit_sequence DOT
				  | digit_sequence DOT digit_sequence
				  | digit_sequence DOT digit_sequence scale_factor
				  | digit_sequence DOT scale_factor
				  | digit_sequence scale_factor'''
	pass

def p_scale_factor(p):
	'''scale_factor : digit_sequence DOT
				  | digit_sequence DOT digit_sequence
				  | digit_sequence DOT digit_sequence scale_factor
				  | digit_sequence DOT scale_factor
				  | digit_sequence scale_factor'''
	pass

def p_unsigned_digit_sequence(p):
	'''unsigned_digit_sequence : digit
								| unsigned_digit_sequence digit'''
	pass

def p_digit_sequence(p):
	'''digit_sequence : sign unsigned_digit_sequence
						| unsigned_digit_sequence'''
	pass


def p_sign(p):
	'''sign : PLUS
			| MINUS'''
	pass

def p_letter(p):
	'letter : LETTER'
	pass

def p_digit(p):
	'digit : NUMBER'
	pass

def p_string(p):
	'string : QUOTE string_character_list QUOTE'
	pass

def p_string_character_list(p):
	'''string_character_list : string_character
							 | string_character_list string_character'''
	pass

def p_string_character(p):
	'''string_character : ANY_CHARACTER_EXCEPT_QUOTE
						| SQUOTE SQUOTE'''
	pass

def p_label(p):
	'label : integer_number'
	pass

def p_constant(p):
	'''constant : sign constant_identifier
				| sign number 
				| constant_identifier 
				| number 
				| string'''

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) +" INDEX: "+ str(p.lexpos))
			print ("NO SE ESPERABA EL Token " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(p.lexer.lineno))
			print ("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
	else:
		raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.txt'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	#input()