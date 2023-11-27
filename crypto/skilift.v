//WIP verilog code for glacierCTF 2023. Doesn't work yet.

module add_and_xor(
    output reg [63:0] result
);

    // Hardcoded 64-bit constants
    reg [63:0] constant1 = 64'h5443474D489DFDD3; // Output from the previous challenge
    reg [63:0] constant2 = 64'h12345678; // From the last step in the challenge

    // Stage 1: Addition
    always @* begin
        result = constant1 + constant2;
    end
    
    // Stage 2: Bitwise XOR
    always @* begin
        result = result ^ 64'h4841434B45525321; // XOR with a constant value ("HACKERS!" in hexadecimal)
    end
    
    // Stage 3: Bitshift
    always @* begin
        result = result >> 5; // Corrected to use >> for right shift
    end
    
    // Display the result at the end
    initial begin
        $display("Result: %h", result);
    end

endmodule