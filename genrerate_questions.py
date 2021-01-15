from QuestionsGeneration import generate_questions as gq

def generate(textlist):
    res = gq.gen_questions(textlist)
    print(res)
    return res

if __name__ == "__main__":
    text =  [
        "Quantum computers promise an exponential growth in processing power capable of tackling problems . Computationally power is off the charts what's about to happen with quantum computing is going to make the past look incredibly slow . Tech giants like ibm and google and startups like brigade computing are all in something of a scientific race to build the first universal quantum computer . To fully understand what makes a quantum computer so uniquely powerful you'll need to know a bit of quantum mechanics. To understand why quantum computers don't really obey the same rules that the world around us does we use we use the laws of the world to solve problems such as encryption and quantum computing. We're looking at a hermetically sealed glass laboratory in the hope of creating a universal quantum computers that could power the next computing revolution. We want to use the technology of the teacher to create a new generation of quantum computing",
        "There's a very special form of superposition known as entanglements . entanglement when we talk about classical computing we often hear the word bit and bit can refer to zero and one . Instead of using these bits via zero or ones we use what's called qubits which are quantum bits in these bits instead of being a zero or one can neither be sort of any combination of a zero under one this is something that sort of arises because of quantum mechanics but it allows us to do more tricks now . controlling qubits and constructing the right quantum architecture are today's major engineering challenges which is why quantum computers in the labs that house them today look like this white where computers were in the fifties or forties or where you had technicians plugging and unplugging things all over the place on some wall electricity on wall electricity was in the 1950s or the forties . Control qubits is today's",
        "Rage ibm and other tech companies are investing in something called superconducting qubits a supercontinent is just metal on a silicon ship and that metal on the second ship is arranged in such a way that when you cool it down to a low enough temperature that the metal becomes superconnecting and that is all the electrons can flow without electrical resistance they can actually take on individual quantum states . The most noticeable sound you hear in our labs is the cryocores they work by pulsing helium gas into and out of this refrigerator system . There's an entire suite of hardware components and coaxio cables attenuators atteniators attenuator microwave amplifiers circulators and circulators a whole bevy of components that are all need to function at low temperatures to enable our quantum computers to work at low speeds to enable the computers . The world's largest quantum computer is now being built by",
        "Quantum processors in order to sort of control the cubits we have a lot of hardware that sends pulses and signals to the qubits we use this thing which we call a resonator which is sensitive to the state of the cubit . The amount of time acute that can retain its quantumness is still pretty short . The single biggest challenge all the time is always how do you make these cubists last as long as possible coherent times is how long quantum information lasts inside of a cubit so if you put a cupboard from this to this to the one state and you just wait hundreds two hundred microseconds at some point that extra little bit of energy will decay out of tubital of the noise will decay . At this stage the amount of . energy . will decay in the quantum algorithms still not quite good enough to perform these quantum algorithms in a head to head match between quantum computers",
        "Quantum computers are still in the experimental stage but their raw potential and imminent arrival are sure to cause a paradigm shift in computing physics and potentially our understanding of the world we live in today . Quantum computers can analyze large quantities of data and spot patterns quickly they could tackle optimization problems for transportation and industry advanced climate modeling and boost artificial intelligence research one day but for those wondering when they'll be able to pick up a quantum laptop you won't have sort of a personal laptop that is a quantum computer will be a little bit more behind the scenes quantum computers will be more behind-the-scenes but quantum computers won't be available for purchase until the end of the next generation of generations of computing technology is ready to be developed . For more science documentaries check out this one right here don’t forget to subscribe to subscribe and keep coming back to the subscribe"

    ]
    r = generate(text)
    print(r)
