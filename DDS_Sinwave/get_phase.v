module get_phase
(
	input [31:0] frequency,
	input clk_200M,
	input rst_n,
	
	output reg [31:0] phase
);

	wire [48:0] temp = frequency * 24'd5629500;
	wire [31:0] K_12_20 = temp[48:18];
	
	always @(posedge clk_200M or negedge rst_n) begin
		if(!rst_n) begin
			phase <= 0;
		end
		else begin
			phase <= phase + K_12_20;
		end
	end

endmodule