library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity freq_div is
	generic(
		CLK_INPUT 		:integer :=  125000000;	  -- The board clock in Hz
		CLK_OUTPUT	 	:integer :=  2	          -- The desired clock in Hz					        
	);
	port(
		clk_in 	: in 	std_logic;
		clk_out	: out std_logic
	);
end freq_div;

architecture Behavioral of freq_div is

	-- Constants
	constant CLK_DIVISOR :integer :=  ((CLK_INPUT / CLK_OUTPUT) / 2);	-- Frequency divisor factor
	
	-- Signals
	signal clk		  : std_logic := '0';
	signal clk_count : integer range 0 to CLK_DIVISOR-1;
	
begin

	-- FREQUENCY DIVIDER
	CLK_DIV: process (clk_in)
	
	begin
	
		if(clk_in'event and clk_in = '1') then
			if(clk_count = CLK_DIVISOR-1) then
				clk <= not clk;
				clk_count <= 0;
			else
				clk_count <= clk_count + 1;
			end if;
		end if;

	end process CLK_DIV;

	clk_out <= clk;
		
end Behavioral;